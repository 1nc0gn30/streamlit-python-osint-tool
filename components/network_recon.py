import streamlit as st
import subprocess

def run_command(command):
    """Run a shell command and return its output."""
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

def network_recon_component():
    st.header("Network Recon: dig, whatweb, wpscan")

    # dig DNS Lookup
    st.subheader("DNS Lookup (dig)")
    domain = st.text_input("Enter domain for DNS lookup:")
    if st.button("Run dig"):
        if domain:
            dig_result = run_command(f"dig {domain}")
            st.text_area("dig Output", dig_result, height=200)
        else:
            st.warning("Please enter a domain.")

    # WhatWeb Technology Scan
    st.subheader("WhatWeb Technology Scan")
    url = st.text_input("Enter URL for WhatWeb scan:")
    if st.button("Run WhatWeb"):
        if url:
            whatweb_result = run_command(f"whatweb {url}")
            st.text_area("WhatWeb Output", whatweb_result, height=200)
        else:
            st.warning("Please enter a URL.")

    # WPScan for WordPress Sites
    st.subheader("WordPress Scan (WPScan)")
    wordpress_url = st.text_input("Enter WordPress site URL:")
    wpscan_api_key = st.text_input("Enter your WPScan API key:", type="password")
    if st.button("Run WPScan"):
        if wordpress_url and wpscan_api_key:
            wpscan_result = run_command(
                f"wpscan --url {wordpress_url} --api-token {wpscan_api_key}"
            )
            st.text_area("WPScan Output", wpscan_result, height=200)
        else:
            st.warning("Please provide both the URL and WPScan API key.")
