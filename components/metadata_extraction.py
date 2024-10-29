import streamlit as st
from utils.metadata_extractor import extract_metadata

def metadata_extraction_component():
    st.header("Metadata Extraction")
    uploaded_file = st.file_uploader("Upload a file for metadata extraction:")
    if uploaded_file:
        file_path = f"./{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        metadata = extract_metadata(file_path)
        st.text(metadata)

