# OPMthis
_Application to test OPM algorithms on real event streams_



  * [Getting started](#getting-started)
    + [Installation OPMthis](#installation-opmthis)
      - [Backend](#backend)
    + [Set up OPMthis pipeline](#set-up-opmthis-pipeline)
      - [Examplary event stream](#examplary-event-stream)
  * [Theory and Background](#theory-and-background)
  * [OPMthis Structure](#opmthis-structure)
    + [Backend](#backend-1)
    + [Frontend](#frontend)


## Getting started

### Installation OPMthis
_How to run OPMthis_
#### Backend
- Library dependencies:
  - flask 
  - numpy
  - pm4py
  - pandas
  - kafka-python
  - requests

### Set up OPMthis pipeline
_How to setup the overall pipeline with Webflow, GTM and Kafka_

#### Examplary event stream
_How to generate an event stream from test data: Adidas mode_

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


## OPMthis Structure
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



