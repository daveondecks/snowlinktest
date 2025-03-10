import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL

# ✅ Load Snowflake Secrets from .streamlit/secrets.toml
snowflake_secrets = st.secrets["snowflake"]

# ✅ Create Snowflake Connection
engine = create_engine(
    URL(
        user=snowflake_secrets["user"],
        password=snowflake_secrets["password"],
        account=snowflake_secrets["account"],
        warehouse=snowflake_secrets["warehouse"],
        database=snowflake_secrets["database"],
        schema=snowflake_secrets["schema"],
    )
)

# ✅ Page Config
st.set_page_config(page_title="Animal Database", page_icon="🐾", layout="wide")

st.title("🐾 Animal Records")

# ✅ Fetch Data from Snowflake
def fetch_animals():
    query = "SELECT NAME, SPECIES, AGE, COLOUR, DESCRIPTION FROM ANIMALS"
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    return df

# ✅ Display Data
df = fetch_animals()
st.dataframe(df)

st.success("✅ Connected to Snowflake Successfully!")