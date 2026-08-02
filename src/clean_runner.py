# clean_runner.py - Single-purpose script for GitHub Actions
# This script does ONE thing: fetch JSON, clean it, save it.

import json
import httpx
from pathlib import Path
import sys
PROJECT_ROOT = Path(__file__).resolve().parent.parent  # Adjust this to point to your project root
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from datajson.jsonarrayclean import JSONCleaner


# 1. Define the URL where your raw JSON lives
# CHANGE THIS: Replace with YOUR JSON source URL
URL = 'https://raw.githubusercontent.com/AshuMItter/companies_detail/refs/heads/main/companies.json'

print(f"Fetching data from URL: {URL}")

headers = {
    "Accept": "application/json",
    "User-Agent": "Python HTTPX Client"
}
# 2. Fetch the raw JSON data from the internet
response = httpx.get(URL, headers=headers)
if response.status_code == 200:
    print("🧹 Cleaning JSON data...")

# 3. Create a cleaner instance and clean the data
    cleaner = JSONCleaner()
    jsonData = response.json()
    cleaned_data = cleaner.clean_json(jsonData)
# 4. Save the cleaned data to a file
    output_file = PROJECT_ROOT / "data" / "cleaned_companies.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)
    print(f"✅ Cleaned JSON data saved to: {output_file}")