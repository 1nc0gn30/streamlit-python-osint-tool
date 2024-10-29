from opencage.geocoder import OpenCageGeocode
import streamlit as st
import pandas as pd
import plotly.express as px
import re
from osint.ip_geolocation import ip_geolocation

# Initialize OpenCage Geocoder with your API key
API_KEY = "adfc48f9577645f9b21de1784df4fe04"
geocoder = OpenCageGeocode(API_KEY)

def ip_geolocation_component():
    st.header("🌍 IP Geolocation Lookup")
    st.info("🔍 Enter an IPv4 or IPv6 address to get geolocation information and view it on a map.")

    ip = st.text_input("Enter IP Address:", placeholder="e.g., 8.8.8.8 or 2600:8805:2513:4300::4410")

    if ip and not is_valid_ip(ip):
        st.error("❌ Please enter a valid IPv4 or IPv6 address.")

    if st.button("Locate IP"):
        if ip and is_valid_ip(ip):
            with st.spinner("Fetching geolocation data..."):
                location_data = ip_geolocation(ip)

                if location_data:
                    st.success(f"Location data found for IP: **{ip}**")
                    display_location_data(location_data)
                else:
                    st.error("❌ Unable to retrieve data for the given IP.")
        else:
            st.warning("⚠️ Please provide a valid IP address.")

def is_valid_ip(ip):
    ipv4_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    ipv6_pattern = r"^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|" \
                   r"([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|::[0-9a-fA-F]{1,4}|" \
                   r"([0-9a-fA-F]{1,4}:){1,5}((:[0-9a-fA-F]{1,4}){1,2})|" \
                   r"([0-9a-fA-F]{1,4}:){1,4}((:[0-9a-fA-F]{1,4}){1,3})|" \
                   r"([0-9a-fA-F]{1,4}:){1,3}((:[0-9a-fA-F]{1,4}){1,4})|" \
                   r"([0-9a-fA-F]{1,4}:){1,2}((:[0-9a-fA-F]{1,4}){1,5})|" \
                   r"[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$"

    return re.match(ipv4_pattern, ip) or re.match(ipv6_pattern, ip)

def display_location_data(data):
    st.subheader("📋 IP Location Details")
    df = pd.DataFrame([data])
    st.dataframe(df, width=800)

    if "lat" in data and "lon" in data:
        display_map(data["lat"], data["lon"])

def display_map(latitude, longitude):
    """Display an interactive map with the IP location using OpenCage."""
    results = geocoder.reverse_geocode(latitude, longitude)

    if results:
        address = results[0]['formatted']
        st.subheader("🗺️ Location on Map")
        st.write(f"**Approximate Address:** {address}")

        fig = px.scatter_mapbox(
            lat=[latitude],
            lon=[longitude],
            hover_name=[address],
            zoom=5,
            height=400,
        )

        fig.update_layout(
            mapbox_style="open-street-map",
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("❌ Unable to retrieve address for the given coordinates.")
