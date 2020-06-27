import json
json_string = json.loads("""{
  "table": [
    {
      "firstname": "Suhas",
      "lastname": "Manjunath",
      "date_stopped": "02/06/2017"
    },
    {
      "firstname": "Shruthi",
      "lastname": "Shashidhar",
      "date_stopped": "02/04/2019"
    }
  ]
}""")

with open('practiceform.json', 'w') as outfile:
    json.dump(json_string, outfile)