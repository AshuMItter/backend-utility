import logging
import json
from pathlib import Path
import uuid
import random

#securedlog.info("User logged in successfully", extra={"data": user_payload})

secureLogs = logging.getLogger('secure_json_logger')
secureLogs.setLevel('INFO') 

# log to json file

# path = Path(__file__).resolve().parent/"securedlogs"

# if(not path.exists()):
#      path.mkdir(parents=True,exist_ok=True)


# file_handler = logging.FileHandler(path/'backend.json.log',encoding='UTF-8')

file_handle = logging.FileHandler('demo.json.log',encoding='utf-8')


class JSONFormatter(logging.Formatter):
    def format(self, record):
                guid = uuid.uuid4().hex
                log_entry ={
                    "traceId":guid,
                    "timestamp" : self.formatTime(record, "%Y-%m-%dT%H:%M:%S"),
                    "level" :record.levelname,
                    "message": record.getMessage()
                }

                # Inject the scrubbed data dictionary if it exists
                if hasattr(record, "data") and isinstance(record.data, dict):
                     log_entry["payload"] = record.data
            
                return json.dumps(log_entry)

        



file_handle.setFormatter(JSONFormatter())


class JSONSecuerFilter(logging.Filter):
       """Filter that looks for sensitive keys and redacts their values."""
       SENSITIVE_KEYS = {"password", "token", "secret", "cvv"}

       def filter(self, record):
        # Check if custom structured data was passed into the 'extra' parameter
        if hasattr(record, "data") and isinstance(record.data, dict):
            record.data = self._redact(record.data)
        return True

       def _redact(self,data):
               """Recursively loops through a dictionary to mask matching keys."""
               cleaned = {}
               for key, value in data.items():
                  if key.lower() in self.SENSITIVE_KEYS:
                     cleaned[key] = "********"
                  elif isinstance(value, dict):
                     cleaned[key] = self._redact(value)  # Handle nested dictionaries
                  else:
                     cleaned[key] = value
               return cleaned
             

file_handle.addFilter(JSONSecuerFilter())


secureLogs.addHandler(file_handle)


# 
user_payload = {
    "username": "alice_dev",
    "secret":"some_secret",
    "auth": {
        "token": "ghp_secret_string_12345",
        "method": "OAuth"
    },
    "session_id": 98421
}

secureLogs.info("User logged in successfully", extra={"data": user_payload})




# import logging
# import json
# from pathlib import Path
# import uuid;

# secureJsonlogger = logging.getLogger('secure_json_logger')
# # set minimum log leve
# secureJsonlogger.setLevel('INFO')


# path = Path(__file__).resolve().parent/"securedlogs"

# if(not path.exists()):
#      path.mkdir(parents=True,exist_ok=True)


# file_handler = logging.FileHandler(path/'backend.json.log',encoding='UTF-8')



# class JSONFormatter(logging.Formatter):
#         """Formatter that converts the log record and data into a single JSON line."""
#         def format(self, record):
#                 log_entry ={
#                      "traceId":uuid.uuid4(),
#                         "timestamp" : self.formatTime(record, "%Y-%m-%dT%H:%M:%S"),
#                         "level" :record.levelname,
#                         "message": record.getMessage()
#                 }

#                 # Inject the scrubbed data dictionary if it exists
#                 if hasattr(record, "data") and isinstance(record.data, dict):
#                      log_entry["payload"] = record.data
            
#                 return json.dumps(log_entry)

# file_handler.setFormatter(JSONFormatter())

# class JSONSensitiveFilter(logging.Filter):
#        """Filter that looks for sensitive keys and redacts their values."""
#        SENSITIVE_KEYS = {"password", "token", "secret", "cvv"}

#        def filter(self, record):
#         # Check if custom structured data was passed into the 'extra' parameter
#         if hasattr(record, "data") and isinstance(record.data, dict):
#             record.data = self._redact(record.data)
#         return True

#        def _redact(self,data):
#                """Recursively loops through a dictionary to mask matching keys."""
#                cleaned = {}
#                for key, value in data.items():
#                   if key.lower() in self.SENSITIVE_KEYS:
#                      cleaned[key] = "********"
#                   elif isinstance(value, dict):
#                      cleaned[key] = self._redact(value)  # Handle nested dictionaries
#                   else:
#                      cleaned[key] = value
#                return cleaned
              
             
# file_handler.addFilter(JSONSensitiveFilter())
       


# secureJsonlogger.addHandler(file_handler)


# secureJsonlogger.info("Application setup complete.")

# # 2. Log with sensitive nested dictionary payload
# user_payload = {
#     "username": "alice_dev",
#     "auth": {
#         "token": "ghp_secret_string_12345",
#         "method": "OAuth"
#     },
#     "session_id": 98421
# }

# # Always pass your log data through an extra dictionary key (like 'data')
# secureJsonlogger.info("User logged in successfully", extra={"data": user_payload})


# import logging
# import json

# jsonsecurelogger = logging.getLogger('secure_json_logger')

# jsonsecurelogger.setLevel('INFO')

# file_handler = logging.FileHandler('backend2.json.log',encoding='utf-8')


# class JSONFormatter(logging.Formatter):
#     def format(self, record):
#         log_entry={
#             "timestamp":self.formatTime(record,"%Y-%m-%dT%H:%M:%S"),
#             "level":record.levelname,
#             "message":record.getMessage()
#         }

#         if hasattr(record,"data") and isinstance(record.data,dict):
#             log_entry['payload'] = record.data
#         return json.dumps(log_entry)



# class JSONFilter(logging.Filter):
#     """Filter that looks for sensitive keys and redact thier values"""
#     SENSITIVE_KEYS =["token","cvv","password","secret"]
#     def filter(self, record):       

#         if hasattr(record,"data") and isinstance(record.data,dict):
#             record.data = self._redact(record.data)
#         return True

#     def _redact(self,data):
#         cleaned={}
#         for key,value in data.items():
#             if key.lower() in self.SENSITIVE_KEYS:
#                 cleaned[key]= "********"
#             elif isinstance(value,dict):
#                 cleaned[key]= self._redact(value)
#             else:
#                 cleaned[key] = value
#         return cleaned




# file_handler.setFormatter(JSONFormatter())
# file_handler.addFilter(JSONFilter())


# jsonsecurelogger.addHandler(file_handler)


# user_payload = {
#     "username": "alice_dev",
#     "secret":"some of my secrets",
#     "auth": {
#         "token": "ghp_secret_string_12345",
#         "method": "OAuth"
#     },
#     "session_id": 98421
# }


# jsonsecurelogger.info("Application Started Successfully",extra={"data": user_payload})



