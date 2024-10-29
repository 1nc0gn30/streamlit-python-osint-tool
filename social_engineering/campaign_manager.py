import json
import os

# File path for storing campaigns locally
CAMPAIGN_FILE = "./data/campaigns.json"

def load_campaigns():
    """Load campaigns from the JSON file."""
    if os.path.exists(CAMPAIGN_FILE):
        with open(CAMPAIGN_FILE, "r") as file:
            return json.load(file)
    return []  # Return an empty list if no campaigns are found

def save_campaigns(campaign_data):
    """Save campaigns to the JSON file."""
    with open(CAMPAIGN_FILE, "w") as file:
        json.dump(campaign_data, file, indent=4)

def track_campaign(target_name, company_name, message):
    """Track a new phishing campaign."""
    campaign = {
        "target": target_name,
        "company": company_name,
        "message": message,
    }
    campaign_data = load_campaigns()
    campaign_data.append(campaign)
    save_campaigns(campaign_data)

def get_campaign_data():
    """Retrieve all tracked campaigns."""
    return load_campaigns()
