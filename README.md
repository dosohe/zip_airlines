# ZipAirlines

## Presets:
    Clone project from github: git clone git@github.com:dosohe/zip_airlines.git

## Run project with docker-compose:
    docker-compose -p zip_airlines  --file dev/docker-compose.yml up -d --build

## REST APIs Description:
    ● Allow for input of 10 airplanes with user defined id and passenger assumptions
    ● Print total airplane fuel consumption per minute and maximum minutes able to fly

## URL: [post:] `http://localhost:8080/api/airplanes/`
## POST data format:
```json
[
    {
        "airplane_id":1,
        "number_of_passenger":100
    },
    {
        "airplane_id":2,
        "number_of_passenger":200
    },
    {
        "airplane_id":3,
        "number_of_passenger":300
    }
]
```
## Response data:
```json
[
    {
        "airplane_id": 1,
        "number_of_passenger": 100,
        "fuel_consumption_per_minute": 0.2,
        "flight_maximum_minutes": 1000.0
    },
    {
        "airplane_id": 2,
        "number_of_passenger": 200,
        "fuel_consumption_per_minute": 0.9545177444479562,
        "flight_maximum_minutes": 419.0597841964052
    },
    {
        "airplane_id": 3,
        "number_of_passenger": 300,
        "fuel_consumption_per_minute": 1.478889830934488,
        "flight_maximum_minutes": 405.7097340515683
    }
]
```
## Check swagger: `http://localhost:8080/swagger/`

## Check test coverage:
    Go to web container shell: docker exec -it zip_airlines_web_1 bash
    Use the following commands: 
        to run test coverage: coverage run --source='.' manage.py test airplane 
        to check the coverage report: coverage report
        to clear the report: coverage erase
