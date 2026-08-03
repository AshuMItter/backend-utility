
from pathlib import Path
import sys
import os
import platform
import logging
import uuid 
import json 
 
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from logs.logmanager import JsonSecureLogger
from datajson.jsonarrayclean import JSONCleaner
from httpxclient.httpxc import HTTPXClient


# secureJsonlogger.info("User logged in successfully", extra={"data": user_payload})
class StartAutomation:
    def __init__(self,input_url,primary_key):
        self.json_cleaner = JSONCleaner()
        self.http_client = HTTPXClient(input_url)
        self.logger = JsonSecureLogger()
        self.input_url = input_url
        self.primary_key = primary_key
  

    def run(self):       
        try:
            # Fetch JSON data from the provided URL
            response = self.http_client.FetchJsonData()
            if response.status_code ==200:
                json_data = response.json()
                primary_key = str(uuid.uuid4())
                payload_fetched={
                "url": self.input_url,
                "os_info": f"{platform.system()} {platform.release()} ({platform.machine()})", 
                "data": json_data,
                "primary_key": self.primary_key
                }
                self.logger.logCustomLog(logging.INFO, f"Fetched JSON data from {self.input_url}", data=payload_fetched)
                print(f"Fetched JSON data from {self.input_url} successfully. {self.primary_key}")

               # Clean the JSON data
                cleaned_data = self.json_cleaner.clean_json(json_data)
                payload_cleaned={
                            "url": self.input_url,
                            "os_info": f"{platform.system()} {platform.release()} ({platform.machine()})", 
                            "cleaned_data": cleaned_data,
                            "primary_key": self.primary_key
                        }
                self.logger.logCustomLog(logging.INFO, "Cleaned JSON data successfully", data=payload_cleaned)
                print(f"Cleaned JSON data successfully. {self.primary_key}")


                # adding this cleaned data in file 
                with open("cleaned_data.json", "w",encoding='utf-8') as f:
                    f.write(json.dumps(cleaned_data, ensure_ascii=False, indent=4))

            # Further processing can be done here with cleaned_data
            # For example, saving to a file or database

        except Exception as e:
               primary_key = str(uuid.uuid4())
               payload={
                            "url": self.input_url,
                             "os_info": f"{platform.system()} {platform.release()} ({platform.machine()})", 
                             "error": str(e),
                             "primary_key": self.primary_key
                        }
               self.logger.logCustomLog(logging.ERROR, f"Error during automation: {str(e)}", data=payload)
