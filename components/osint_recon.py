import streamlit as st
import time
from osint.recon import search_username
from streamlit_extras.badges import badge

def osint_recon_component():
    st.header("🔍 OSINT Recon")

    # Username Input
    username = st.text_input("Enter a username to search:", placeholder="e.g., johndoe123")

    # Columns for Buttons and Info
    col1, col2 = st.columns([1, 2])

    with col1:
        if st.button("🔍 Search Username"):
            if username:
                with st.spinner("Searching across platforms..."):
                    time.sleep(1)  # Simulate delay for user feedback
                    results = search_username(username)

                    # Display Results
                    st.success(f"Search completed for: **{username}**")

                    # Advanced UI for Results
                    display_results(results)
            else:
                st.warning("Please enter a username to search.")

    with col2:
        st.info("💡 This tool searches for a username across Twitter, GitHub, and Instagram.")

def display_results(results):
    """Display search results in a user-friendly way."""
    st.subheader("Results")

    if not results:
        st.write("No platforms found with this username.")
        return

    for platform, status in results.items():
        col1, col2 = st.columns([1, 9])
        with col1:
            if status == "Found":
                st.success("✅")
            else:
                st.error("❌")

        with col2:
            st.write(f"**{platform}**: {status}")
            badge(platform)  # Add badge for platform name

        st.markdown("---")

