import json
import httpx



class JSONCleaner:
    def __init__(self):
        self.company_defaults= {     
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

    def clean_json(self, json_data):
        if not isinstance(json_data, dict) or "company" not in json_data:
            raise ValueError("Input data must be a dictionary.")


        for key, default_value in self.company_defaults.items():
            print(f"Key: {key}, Default Value: {default_value}")

            if key not in json_data["company"]:
                json_data["company"][key] = default_value

            elif isinstance(default_value, dict):
                for sub_key, sub_default in default_value.items():
                    if sub_key not in json_data["company"][key]:
                        json_data["company"][key][sub_key] = sub_default

        return json_data
            # if key not in json_data["company"]:
            #     json_data["company"][key] = default_value
            # elif isinstance(default_value, dict):
            #     for sub_key, sub_default in default_value.items():
            #         if sub_key not in json_data["company"][key]:
            #             json_data["company"][key][sub_key] = sub_default


   

jsonData ={
"company": {
    "name": "TechInnovate Solutions",
    "founded": 2015,
    "is_active": 'true',
    "rating": 4.8,
    "headquarters": {
      "city": "San Francisco",
      "state": "CA",
      "country": "USA",
      "zip_code": "94105"
    }
}
}

missing_fields_json = {
    "company": {
        "name": "TechInnovate Solutions",
        "founded": 2015,
        "headquarters": {
            "city": "San Francisco"
        }
    }
}
cleaner = JSONCleaner()
cleaned_data = cleaner.clean_json(missing_fields_json)


print("Cleaned JSON Data:")
print(json.dumps(cleaned_data, indent=4))



