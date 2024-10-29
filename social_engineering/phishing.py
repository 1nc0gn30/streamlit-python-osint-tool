import random

def generate_phishing_message(target_name, company_name):
    templates = [
        f"Hi {target_name},\n\nWe noticed suspicious activity in your {company_name} account. Please click the link below to reset your password:\n\nhttps://secure-{company_name.lower()}-support.com/reset",
        f"Dear {target_name},\n\nYour {company_name} subscription is about to expire! Click here to renew:\n\nhttps://renew-{company_name.lower()}-portal.com",
        f"Hello {target_name},\n\nYour {company_name} payroll has encountered an issue. Please confirm your details to avoid delays:\n\nhttps://{company_name.lower()}-payroll.com/verify",
    ]
    return random.choice(templates)

