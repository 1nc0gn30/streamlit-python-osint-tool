import streamlit as st
from osint.shodan_lookup import shodan_search

def shodan_recon_component():
    st.header("Shodan Recon")
    shodan_ip = st.text_input("Enter IP Address for Shodan Lookup:")
    shodan_api_key = st.text_input("Enter your Shodan API key:", type="password")
    if st.button("Search on Shodan"):
        if shodan_ip and shodan_api_key:
            shodan_data = shodan_search(shodan_ip, shodan_api_key)
            st.write(shodan_data)
        else:
            st.warning("Please provide both IP and API key.")

