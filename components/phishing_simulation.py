import streamlit as st
from social_engineering.phishing import generate_phishing_message
from social_engineering.campaign_manager import track_campaign

def phishing_simulation_component():
    st.header("Phishing Simulation")
    target_name = st.text_input("Enter Target's Name:")
    company_name = st.text_input("Enter Company Name:")
    if st.button("Generate Phishing Message"):
        if target_name and company_name:
            message = generate_phishing_message(target_name, company_name)
            st.text_area("Phishing Message", message, height=150)
            track_campaign(target_name, company_name, message)
        else:
            st.warning("Please provide both target's name and company name.")

