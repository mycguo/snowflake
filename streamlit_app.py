# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Get the current credentials
session = get_active_session()

# Write directly to the app
st.title(f"Loading tables from DATAMART_BI_DEV.CUSTOMERSERVICE")

user = session.sql("SELECT current_user() AS user").collect()[0]['USER']
st.markdown(f"Hello. Your current user is: :blue[{user}]")

st.markdown("Let's access the `AGENT_CALLS` table")
df = session.table("DATAMART_BI_DEV.CUSTOMERSERVICE.AGENT_CALLS").limit(1000).to_pandas()
st.dataframe(df)

st.markdown("Let's get all table names from DATAMART_BI_DEV.CUSTOMERSERVICE schema")
tables_df = session.sql("SHOW TABLES IN SCHEMA DATAMART_BI_DEV.CUSTOMERSERVICE").to_pandas()
st.dataframe(tables_df)