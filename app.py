import streamlit as st
import pandas as pd
st.set_page_config(page_title="Municipal Services Explorer", layout="wide")
st.title("Municipal Services Explorer")
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.dataframe(df)
  st.metric("Rows", len(df))
  st.write(df.columns.tolist())
  selected_column = st.selectbox("Select column", options=df.column_names())
  st.write(int(df[selected_column].isna().total()))
  st.metric("Unique values", df[selected_column].nunique())
  numeric_columns = df.select_dtypes(include="number").columns.tolist()
   if len(numeric_columns) > 0:
      numeric_column = st.selectbox("Numeric column", choices=numeric_columns)
      st.line_chart(df[numeric_column])
      st.write(df[numeric_column].describe())
      csv_bytes = df.to_csv(index=False).encode("utf-8")

st.download_button("Download CSV", data=csv_bytes, file_name="services_export.csv", mime="text/csv")


  
  
