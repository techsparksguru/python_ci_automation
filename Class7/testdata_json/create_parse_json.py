import json
json_string = """{
   "desc":{
      "someKey":"someValue",
      "anotherKey":"value"
   },
   "main_item":{
      "stats":{
         "a":8,
         "b":12,
         "c":10
      }
   }
}"""

json_dict = json.loads(json_string)
print("Printing the json")
print("Printing the keys and values")
for i in json_dict:
    print(i, json_dict[i])
print("Accessing some values...")
print(json_dict["desc"]["someKey"])
print(json_dict["main_item"]["stats"]["a"],"\n")