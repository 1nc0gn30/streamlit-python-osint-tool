# OSINT & Social Engineering Toolkit

This toolkit is a web-based OSINT (Open Source Intelligence) and social engineering tool powered by **Streamlit**. It integrates multiple components to assist with reconnaissance, phishing simulations, and more.

## Features

- **OSINT Recon:** Gather public information from multiple sources.
- **Email Breach Checker:** Identify if an email has been part of a breach.
- **IP Geolocation:** Track IP addresses with location data.
- **Shodan Recon:** Use Shodan to gather information on internet-connected devices.
- **Metadata Extraction:** Extract metadata from uploaded files.
- **Phishing Simulation:** Simulate phishing attacks for testing purposes.
- **Campaign Tracker:** Track phishing or social engineering campaigns.
- **Network Recon:** Perform reconnaissance on network configurations.
- **Impacket Component:** Utilize Impacket tools for post-exploitation tasks.
- **TheHarvester Integration:** Gather information from search engines and social networks.

## Prerequisites

- **Python 3.8+** installed.
- **Streamlit** library.
- API keys for services such as Shodan (if applicable).
- Install necessary OSINT tools like **Impacket** and **TheHarvester** if they are not bundled in the project.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/1nc0gn30/streamlit-python-osint.git
   cd https://github.com/1nc0gn30/streamlit-python-osint-tool.git
2. Install Dependencies:

pip install -r requirements.txt


3. Configure API Keys and Environment Variables:

Create .env file in root directory.

Add the required API keys and credentials in the .env file.




Usage

1. Run the Streamlit App:

streamlit run app.py


2. Access the Web Interface:

Open a web browser and navigate to http://localhost:8501. (or whate ever port you are serving)



3. Use the Components:

Perform OSINT tasks such as IP tracking, email breach checks, and Shodan lookups.

Simulate phishing attacks and track campaigns.
