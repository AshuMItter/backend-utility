import json

class JSONCleaner:
    def __init__(self):
        self.company_defaults = {     
            "name": "Unknown Company",
            "founded": 2000,
            "is_active": False,
            "rating": 0.0,
            "headquarters": {
                "city": "Unknown",
                "state": "Unknown",
                "country": "Unknown",
                "zip_code": "00000"
            }
        }

    def _clean_single_company(self, company):
        """Clean a single company object"""
        # Apply defaults for missing fields
        for key, default_value in self.company_defaults.items():
            if key not in company:
                company[key] = default_value
            elif isinstance(default_value, dict):
                # Handle nested dictionaries
                for sub_key, sub_default in default_value.items():
                    if sub_key not in company[key]:
                        company[key][sub_key] = sub_default
        return company

    def clean_json(self, json_data):
        """Clean JSON data - handles both single objects and arrays"""
        
        # Handle empty data
        if not json_data:
            return []
            
        # If it's a single company object (not wrapped in "company" key)
        if isinstance(json_data, dict) and "name" in json_data:
            return self._clean_single_company(json_data)
            
        # If it's wrapped in a "company" key (backward compatibility)
        if isinstance(json_data, dict) and "company" in json_data:
            return self._clean_single_company(json_data["company"])
            
        # If it's an array of companies
        if isinstance(json_data, list):
            cleaned_companies = []
            for company in json_data:
                if isinstance(company, dict):
                    cleaned_companies.append(self._clean_single_company(company))
            return cleaned_companies
            
        # If none of the above, raise error
        raise ValueError("Input data must be a company object, array of companies, or object with 'company' key")

# Test with your array data
array_data = [
    {
        "name": "TechInnovate Solutions",
        "founded": 2015,
        "is_active": True,
        "rating": 4.8,
        "headquarters": {
            "city": "San Francisco",
            "state": "CA",
            "country": "USA",
            "zip_code": "94105"
        }
    },
    {
        "name": "QuickTech",
        "founded": 2023,
        "is_active": True,
        "rating": 4.7,
        "headquarters": {
            "city": "Dallas",
            "state": "TX",
            "country": "USA",
            "zip_code": "75201"
        }
    },
    {
        "name": "QuickTechJapan",
        "founded": 2023,
        "is_active": True,
        "rating": 4.5,
        "headquarters": {
            "city": "Hiroshima",
            "state": "Tk",
            "country": "Japan",
            "zip_code": "4567"
        }
    },
    {
        "name": "QuickTechLondon",
        "founded": 2034,
        "is_active": True,
        "rating": 4.8,
        "headquarters": {
            "city": "Yorkshire",
            "state": "London",
            "country": "UK",
            "zip_code": "456768"
        }
    }
]

# Test with missing fields
missing_fields_array = [
    {
        "name": "TechInnovate Solutions",
        "founded": 2015,
        "headquarters": {
            "city": "San Francisco"
        }
    },
    {
        "name": "QuickTech",
        "rating": 4.7,
        "headquarters": {
            "city": "Dallas",
            "state": "TX"
        }
    }
]

# cleaner = JSONCleaner()

# # Test with complete array
# print("=== Complete Array ===")
# cleaned_array = cleaner.clean_json(array_data)
# print(json.dumps(cleaned_array, indent=4))

# print("\n=== Array with Missing Fields ===")
# cleaned_missing = cleaner.clean_json(missing_fields_array)
# print(json.dumps(cleaned_missing, indent=4))

# # Test with single object
# print("\n=== Single Object ===")
# single_company = {
#     "name": "Test Company",
#     "headquarters": {
#         "city": "Test City"
#     }
# }
# cleaned_single = cleaner.clean_json(single_company)
# print(json.dumps(cleaned_single, indent=4))

# # Test with empty data
# print("\n=== Empty Data ===")
# empty_data = []
# cleaned_empty = cleaner.clean_json(empty_data)
# print(cleaned_empty)