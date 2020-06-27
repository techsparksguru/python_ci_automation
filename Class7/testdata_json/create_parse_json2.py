import json
json_array = json.loads("""{
    "menu": {
    "id": "file",
    "value": "File",
    "popup": {
      "menuitem": [
        {
          "value": "New",
          "onclick": "CreateNewDoc()"
        },
        {
          "value": "Open",
          "onclick": "OpenDoc()"
        },
        {
          "value": "Close",
          "onclick": "CloseDoc()"
        }
      ]
    }
  }
}""")

print(json_array)
for i in json_array:
   print(i, json_array[i])
   print("Accessing menuitem array...")
   print(json_array["menu"]["popup"]["menuitem"])
   print("Printing menitem array elements...")
   temp_array = json_array["menu"]["popup"]["menuitem"]
   for j in temp_array:
       print(j)
   print("Accessing a menuitem element as json..")
   print(temp_array[0]["value"])
   print(temp_array[2]["value"])
   print(temp_array[1]["onclick"])