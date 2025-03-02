import streamlit as st
import pandas as pd
import dask.dataframe as dd
import polars as pl
import time
from faker import Faker

# Initialize Faker
fake = Faker()

# Streamlit App Title
st.title("🚀 Data Processing with Pandas, Dask, and Polars")

# Sidebar settings
st.sidebar.header("⚙️ Dataset Configuration")
num_rows = st.sidebar.slider("📊 Number of rows", min_value=100, max_value=1_000_000, value=100_000, step=10_000)

# Generate synthetic dataset using Faker (optimized)
@st.cache_data
def generate_fake_data(n):
    return pd.DataFrame({
        "name": [fake.name() for _ in range(n)],
        "email": [fake.email() for _ in range(n)],
        "address": [fake.address() for _ in range(n)],
        "age": [fake.random_int(min=18, max=80) for _ in range(n)],
        "salary": [fake.random_int(min=30_000, max=120_000) for _ in range(n)]
    })

# Generate dataset
st.write("📌 **Generating dataset...**")
start_time = time.time()
df_pandas = generate_fake_data(num_rows)
st.success(f"✅ Dataset with {num_rows:,} rows generated in {time.time() - start_time:.2f} sec!")

# Convert dataset to Dask and Polars
df_dask = dd.from_pandas(df_pandas, npartitions=4)
df_polars = pl.DataFrame(df_pandas)  # Convert Pandas → Polars

# Function to compute average salary by first letter
def compute_average_salary(df, lib):
    start_time = time.time()
    
    if lib == "pandas":
        df["first_letter"] = df["name"].str[0]
        result = df.groupby("first_letter")["salary"].mean().reset_index()
    elif lib == "dask":
        df["first_letter"] = df["name"].str[0]
        result = df.groupby("first_letter")["salary"].mean().compute().reset_index()
    elif lib == "polars":
        df = df.with_columns([
            pl.col("name").str.slice(0, 1).alias("first_letter"),
            pl.col("salary").cast(pl.Float32)  # Force consistent precision
        ])
        result = df.group_by("first_letter").agg(pl.col("salary").mean()).to_pandas()
    elapsed_time = time.time() - start_time
    return result, elapsed_time

# Compute transformations for each library
st.subheader("💡 Transformation: Average Salary by First Letter of Name")

result_pandas, time_pandas = compute_average_salary(df_pandas, "pandas")
result_dask, time_dask = compute_average_salary(df_dask, "dask")
result_polars, time_polars = compute_average_salary(df_polars, "polars")

# Display results side by side
st.write("📊 **Comparison of Results Across Libraries**")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🐼 Pandas")
    st.write(f"⏳ **Execution Time:** {time_pandas:.4f} sec")
    st.write(result_pandas.head())

with col2:
    st.subheader("🟡 Dask")
    st.write(f"⏳ **Execution Time:** {time_dask:.4f} sec")
    st.write(result_dask.head())

with col3:
    st.subheader("🦾 Polars")
    st.write(f"⏳ **Execution Time:** {time_polars:.4f} sec")
    st.write(result_polars.head())