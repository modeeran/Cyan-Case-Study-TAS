# Cyan Case Study


## How to use the project

Python 3.11.5, Selenium, Behave, and Request are required. You can install Selenium, Behave, and Request using
`pip install -r requirements.txt`

### Running exercise 1 and 2 locally on Chrome in Docker

Install docker: https://docs.docker.com/engine/install/


#### x86 (or similar) based architecture machine

Run the docker compose for the x86 based machine if you have such computers (e.g., AMD64, Intel). This will be based on selenium/node-chrome image.

```
docker compose -f docker-compose.yml up -d
```


#### Arm based architecture machine

Run the docker compose for the ARM based machine if you have such computers (e.g., Mac M1, M2, M3). This will be based on seleniarm/node-chromium image.
Note: Google does not build Chrome for Linux ARM platforms. Instead, docker-seleniarm uses the open source Chromium browser instead, which is built for ARM.
See more info https://github.com/seleniumhq-community/docker-seleniarm

```
docker compose -f docker-compose-arm.yml up -d
```


The tests take the configuration over environment variable:

- `SELENIUM_EXECUTOR` tells where the selenium server is. If it sets as "local" (or not set),
the tests will be executed on your local machine. If it sets as "hub", the tests will be executed on the selenium/hub docker container.
You can set this variable depending on how you want to run the tests
and then call the test using `behave --tags=[tag]` or `behave`. The tags can be either of `login`, and `status`.

#### Example running in docker container
```
export SELENIUM_EXECUTOR=hub
behave --tags=login
```


### Running exercise 1, 2, and 3 on local machine

 We can run a test or group of tests by going to the main directory of the project and running a related
command:

```
export SELENIUM_EXECUTOR=local
behave --tags=status
behave --tags=api
behave --tags=login
```

### Running the project using a custom docker image including dependencies and configurations
In this way you can have a standalone environment to run the tests. You can create an image using the given Dockerfile. Note: chromedriver has a problem on Linux-based
containers at the moment. 

