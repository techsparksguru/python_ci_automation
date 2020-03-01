Instructions for working with the flask application locally

## Pre-Requisites
Make sure python3.x and pip are installed on your test system

Clone the repository from the below link:
```
https://github.com/techsparksguru/python_ci_automation
```

Navigate to the folder Class5/flask_api and execute the below instructions:

## Create a virtual environment
```cmd
pip install virtualenv

virtualenv venv

\venv\Scripts\activate.bat

`Example:` C:\Users\'Username'\venv\Scripts\activate.bat
```

## Installing the requirements for the application:
```cmd
pip install -r requirements.txt
```

## Running the Flask app
```cmd
python app.py
```

Application will be accessible on PORT 3000

```
http://localhost:3000
```

Download curl CLI app from the below link:

```https://curl.haxx.se/windows/```


Use the below command to get all the routes in the application:
```
curl -L -X GET -H 'Content-Type: application/json' 'localhost:5000/config/routes'
```