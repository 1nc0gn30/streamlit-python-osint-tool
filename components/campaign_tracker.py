import streamlit as st
import pandas as pd
import plotly.express as px
from social_engineering.campaign_manager import get_campaign_data

def campaign_tracker_component():
    st.header("📊 Phishing Campaign Tracker")

    campaigns = get_campaign_data()
    if not campaigns:
        st.info("No campaigns tracked yet.")
        return

    df = pd.DataFrame(campaigns)

    search_target = st.text_input("🔍 Search by Target Name:")
    if search_target:
        df = df[df["target"].str.contains(search_target, case=False, na=False)]

    st.subheader("📋 Campaign Data")
    st.dataframe(df, width=800, height=300)

    st.subheader("📈 Campaign Statistics")
    if not df.empty:
        fig = px.bar(
            df,
            x="company",
            title="Phishing Campaigns by Company",
            labels={"x": "Company", "y": "Number of Campaigns"},
            height=400,
        )
        st.plotly_chart(fig)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Campaign Data as CSV",
        data=csv,
        file_name="phishing_campaigns.csv",
        mime="text/csv",
    )
