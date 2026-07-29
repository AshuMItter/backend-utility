import json
from pathlib import Path


josnPath = Path(__file__).parent.parent/"datajson"/"practice_data.json"

directoryW = Path(__file__).resolve().parent.parent/"datajson"/ "demo.json"

names = {
    "DemoName":
            {"id":1,"name":"demo"}
         }

someData = json.dumps(names)

print(someData)

data = json.loads(josnPath.read_text(encoding='utf-8'))

#print(data)

# print(data['company']['name'])
# name = data['company']['name']
# foundedin = data['company']['founded']

# print(f"The name of the compnay is {name} and It was founded in {foundedin}")

departments = data['company']['departments']

print(type(departments))




for department in departments:
    print(department['head'])
# pathv = Path(__file__).resolve().parent.parent / "datajson"/ "practice_data.json"

# pathvNames = Path(__file__).resolve().parent.parent / "datajson"/ "names.json"




# data = json.loads(pathv.read_text(encoding='utf-8'))

# data2 = json.loads(pathvNames.read_text(encoding='utf-8'))

# print(f"Data from practice_data.json: ",  data['company']['name'], data['company']['founded'])
# companyName = data['company']['name']
# companyFounded = data['company']['founded'] 
# companyHeadquarters = data['company']['headquarters']['city']
# print(f"Company Name: {companyName}, Founded: {companyFounded}, Headquarters: {companyHeadquarters}")

# print(type(data['company']['departments']) )


# print(type(data2['data']['user2']['isActive']) )

# for department in departments:
#     print(f"Department Name: {department['name']}, Employees: {department['employees']}")
#     print(type(department['employees']) )