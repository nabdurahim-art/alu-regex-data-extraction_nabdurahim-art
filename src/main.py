import re
import json


#code to open and read the raw text file
with open("../input/raw-text.txt", "r") as file:
    raw_text = file.read()

#Regex patterns.

# Find valid ALU email addresses only
alu_email_regex = r'\b[A-Za-z0-9._%+-]+@(?:alueducation\.com|alumni\.alueducation\.com|si\.alueducation\.com)\b'


# Find phone numbers
phone_regex = r'(?:\+250|0)\s?\d{3}[\s-]?\d{3}[\s-]?\d{3}'


# Find website links
website_regex = r'https?://[^\s]+'


# Find credit card numbers
card_regex = r'\b(?:\d{4}[- ]?){3}\d{4}\b'


#code to  extract valid data
valid_emails = re.findall(alu_email_regex, raw_text)

valid_phones = re.findall(phone_regex, raw_text)

valid_websites = re.findall(website_regex, raw_text)


#  code to hide sensitive card information
safe_cards = [
    "****-****-****-" + card.replace(" ", "-")[-4:]
    for card in re.findall(card_regex, raw_text)
]


#code to  check for unsafe input
if "<script>" in raw_text or "DROP TABLE" in raw_text:
    print("\nSecurity Alert: Unsafe content detected in the text.")


# code to show results
print("\nValid ALU Emails:")
print(valid_emails)

print("\nValid Phone Numbers:")
print(valid_phones)

print("\nValid Websites:")
print(valid_websites)

print("\nProtected Credit Cards:")
print(safe_cards)


# SAVE RESULTS TO JSON FILE

output_data = {
    "emails": valid_emails,
    "phone_numbers": valid_phones,
    "websites": valid_websites,
    "credit_cards": safe_cards
    }
with open("../output/sample-output.json", "w") as json_file:
    json.dump(output_data, json_file, indent=4)


print("\nResults saved.")
