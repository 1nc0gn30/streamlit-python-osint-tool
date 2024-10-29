import streamlit as st
from components.osint_recon import osint_recon_component
from components.email_breach import email_breach_component
from components.ip_geolocation import ip_geolocation_component
from components.shodan_recon import shodan_recon_component
from components.metadata_extraction import metadata_extraction_component
from components.phishing_simulation import phishing_simulation_component
from components.campaign_tracker import campaign_tracker_component
from components.network_recon import network_recon_component
from components.impacket_component import impacket_component
from components.the_harvester_component import theharvester_component
st.title("OSINT & Social Engineering Toolkit")

# Render each component
osint_recon_component()
email_breach_component()
ip_geolocation_component()
shodan_recon_component()
metadata_extraction_component()
phishing_simulation_component()
campaign_tracker_component()
network_recon_component()
impacket_component()
theharvester_component()

