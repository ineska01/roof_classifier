import streamlit as st

st.write("# Załaduj zdjęcie dachu")

file = st.file_uploader(" ", type=["png", "jpg", "tif"])


if file is not None:
    st.image(file, output_format="auto")
