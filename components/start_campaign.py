import streamlit as st
from social_engineering.campaign_manager import track_campaign

def start_campaign_component():
    st.header("🚀 Start a New Phishing Campaign")

    target_name = st.text_input("Target Name")
    company_name = st.text_input("Company Name")
    message = st.text_area("Phishing Message", height=150)

    if st.button("Start Campaign"):
        if target_name and company_name and message:
            track_campaign(target_name, company_name, message)
            st.success("Campaign started and saved successfully!")
        else:
            st.warning("Please fill in all fields to start a campaign.")
