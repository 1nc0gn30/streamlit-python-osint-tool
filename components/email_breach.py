import streamlit as st
from osint.email_lookup import email_breach_lookup
import re

def email_breach_component():
    st.header("🔐 Email Breach Lookup")
    st.info("💡 Enter an email address to check if it has been part of any known breaches using the HaveIBeenPwned API.")

    # Input Fields
    email = st.text_input("📧 Email:", placeholder="e.g., johndoe@example.com")
    api_key = st.text_input("🔑 API Key:", type="password", placeholder="Enter your API key")

    # Validate Email Input
    if email and not is_valid_email(email):
        st.error("❌ Please enter a valid email address.")

    # Button to Trigger Breach Lookup
    if st.button("🔍 Check Email Breaches"):
        if email and api_key and is_valid_email(email):
            with st.spinner("Checking for breaches..."):
                breaches = email_breach_lookup(email, api_key)

                if breaches:
                    display_breach_results(breaches)
                else:
                    st.success("✅ No breaches found for this email!")
        else:
            st.warning("⚠️ Please provide both a valid email and API key.")

def is_valid_email(email):
    """Simple email validation function."""
    regex = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(regex, email) is not None

def display_breach_results(breaches):
    """Display breach results with pagination and styling."""
    st.warning("⚠️ Breaches Found! Take action immediately.")
    
    # Pagination for large result sets using session state
    if 'page' not in st.session_state:
        st.session_state.page = 0

    per_page = 5  # Results per page
    total_pages = (len(breaches) - 1) // per_page + 1

    # Paginate the results
    start = st.session_state.page * per_page
    end = start + per_page
    current_page_breaches = breaches[start:end]

    # Display Current Page Results
    for breach in current_page_breaches:
        st.write(f"🛡️ **Breach:** {breach}")

    # Pagination Controls
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("⬅️ Previous", key="prev"):
            if st.session_state.page > 0:
                st.session_state.page -= 1

    with col2:
        st.write(f"Page {st.session_state.page + 1} of {total_pages}")

    with col3:
        if st.button("➡️ Next", key="next"):
            if st.session_state.page < total_pages - 1:
                st.session_state.page += 1
