import streamlit as st
import subprocess

def theharvester_component():
    st.header("🔍 theHarvester: OSINT Data Collector")

    # Input Field for Domain
    domain = st.text_input("Enter Domain to Search:", placeholder="e.g., example.com")
    limit = st.slider("Result Limit", min_value=10, max_value=100, value=50, step=10)
    search_engine = st.selectbox("Select Search Engine:", ["google", "bing", "duckduckgo", "yahoo"])

    # Run theHarvester
    if st.button("Run theHarvester"):
        if domain:
            with st.spinner("Collecting OSINT data..."):
                command = f"theHarvester -d {domain} -l {limit} -b {search_engine}"
                output = run_command(command)
                st.text_area("theHarvester Output", output, height=400)
        else:
            st.warning("⚠️ Please enter a domain to search.")

def run_command(command):
    """Run shell commands and return output."""
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"
