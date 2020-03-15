 
# Installing Postman
Follow the instructions at below link 
```
https://www.getpostman.com/
```

# Import collections
Clone the repository or download the zip of it
```
https://github.com/techsparksguru/python_ci_automation
```

# Import the postman collection
1. Open postman tool
2. Import collection
3. Use file `<path to the collection file to be imported>`


# WORKING WITH Newman

## Installing Newman with NPM
```
npm install -g newman
```

## Running the postman collection using newman
```
newman run <path to your api collection json file> -e <path to the environment to be used > -n <iteration_number>
```
