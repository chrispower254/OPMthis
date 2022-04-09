# OPMthis
_Application to test OPM algorithms on real event streams_



  * [Getting started](#getting-started)
    + [Installation](#installation)
      - [Backend](#backend)
    + [Set up OPMthis pipeline](#set-up-opmthis-pipeline)
      - [Examplary event stream](#examplary-event-stream)
  * [Theory and Background](#theory-and-background)
  * [OPMthis Structure](#opmthis-structure)
    + [Backend](#backend-1)
    + [Frontend](#frontend)

---

## Getting started

### Installation
_How to run OPMthis_

0) Requirements
    - Python and pip needs to be installed
    - npm and nodejs has to be installed 
1) Clone repository
2) Install dependencies
    - Backend: Install the following python libraries
        - ```pip install flask```
        - ```pip install numpy```
        - ```pip install pm4py```
        - ```pip install pandas```
        - ```pip install kafka-python```
        - ```pip install requests```
    - Frontend: Navigate in terminal to ./frontend and run ```npm install```
3) Run app
    - Backend: Run backend/main.py
    - Frontend: Navigate with terminal to ./frontend and run ```npm start```

### Set up _OPMthis_ pipeline
_How to setup the overall pipeline with Webflow, GTM and Kafka_

_OPMthis_ is designed to run with event streams coming from Apache Kafka. Obviously this can be changed towards some other stream generation. In this section, we briefly provide information on how to run _OPMthis_ with Kafka.

1) Source
    - You need to have use some website, where you can run JavaScript on
    - In our example, we used a webflow page, since its especially easy to use GTM there
    - **If you don't have an appropriate source** you can also test _OPMthis_ by using a fake stream:
        - The repository provides the event log ```adidas.csv```, you can use this to generate an event stream by simply setting ```source = 'kafka'``` in ./backend/main.py
        - Once you've done this, you can skip step 2 (You still need Kafka for this)
2) Send events with GTM
    - You have to fetch events from your source and pass them into a system for event stream generation
        - For this you can use Google Tag Manager
        - GTM has to be set up to send events to a Kafka host on specific triggers, e.g. on page initializiation
            - LINK TO SEPARATE TUTORIAL
3) Event stream with Apache Kafka
    - In order to process the events from your source, you need to have a system to generate an event stream, e.g. Apache Kafka
    - Install zookeeper, kafka and kafka-rest
    - Run following commands in appropriate directory (property files can be edited to create kafka host locally)
        - ```zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties```
        - ```kafka-server-start /usr/local/etc/kafka/server.properties```
        - ```bin/kafka-rest-start etc/kafka-rest/kafka-rest.properties```

#### Manage settings in config.json

The most important settings can be edited in the ```config.json``` file. You can edit this by using the frontend, or directly navigate to it in the repo.
Explanation fields:
- baseUrl: String that is being removed at the beginning from each activity name -> with 'adidas.com' you would get 'cart' instead of 'adidas.com/cart' 
- eventAttributes: Array that shows the names of names of the attributes that will be sent to _OPMthis_
    - Important(**!**): First three attributes have to be case ID, activity name and timestamp (in this order)
- filters: Based on the eventAttributes, the event stream can be filtered for (each attribute receives an array of strings)
- kafkaSettings: Determines where the Kafka consumer will listen
- opmSettings: Options to use different OPM techniques
    - Only certain combinations are possible, use the frontend to see those combinations

---

## Theory and Background
_OPMthis_ can be used to mine even streams. Refer to "Control-flow discovery from event streams" by A. Burattin, A. Sperduti and W. M. P. van der Aalst (2014) for scientific background.
This application is meant to serve as a basis to test all kinds of OPM activities.
It can easily be extended towards:
- Other sources
- Other OPM algorithms
- Other process diagrams
- Other UIs
- Other use-cases in general

To make _OPMthis_ work, this pipeline needs to be in place:

![Application diagrams-Pipeline drawio](https://user-images.githubusercontent.com/46896615/162034156-b9a3559e-bb90-4c29-9504-22e8320ffbd6.png)

The different pipeline modules are supposed to be as independent from each other as possible. They can be realized with different solutions. This first base version runs with the following setup:
![Application diagrams-OPMThis Pipeline drawio](https://user-images.githubusercontent.com/46896615/162033661-effa5432-e9ca-4960-a873-4cdfbf17cf02.png)


## _OPMthis_ Structure
_OPMthis_ consists of a backend and a frontend. The frontend is only meant to provide an environment to easily test and evaluate OPM approaches. 
This application is structured as the following:

![ModuleView drawio](https://user-images.githubusercontent.com/46896615/161813919-cefa9fed-a7a1-4796-900d-511ce8121a35.png)




### Backend
The backend has two tasks: 
1) Managing the event stream 
2) Providing OPM capabilities

The events are fetched using a Kafka consumer. The incoming messages are stored in a CSV file to build an event log.
The frontend can trigger the app to compute process nets using the pm4py library (http://pm4py.org/). In order to call these functionalities, a Flask server is set up.
Since the Flask server and the Kafka consumer have to coexist during runtime, the app uses multiprocessing.

All settings regarding the event stream and the available OPM techniques are managed in the config.json.

A detailled overview of the structure can be seen in this diagram: _(click to expand)_
![Application diagrams-Backend Overview drawio](https://user-images.githubusercontent.com/46896615/162574285-c6af8c71-f55d-4582-b749-04795fbab1b7.png)

### Frontend

The frontend is created using React in order to provide a webapp. The communication is done via the Flask server. 



