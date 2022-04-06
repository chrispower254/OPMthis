# OPMthis
_Application to test OPM algorithms on real event streams_


- [Background](#background)
- [OPMthis Structure](#opmthis-structure)
- [Installation OPMthis](#installation-opmthis)
- [Getting started OPMthis pipeline](#getting-started-opmthis-pipeline)
  - [Examplary event stream](#examplary-event-stream)


## Background
_OPMthis_ can be used to mine even streams. It is meant to serve as a basic application that can be extended towards
- Other sources
- Other OPM algorithms
- Other process diagrams
- Other UIs
- Other use-cases in general

To make OPMthis work, this pipeline needs to be in place:

![Application diagrams-Pipeline drawio](https://user-images.githubusercontent.com/46896615/162034156-b9a3559e-bb90-4c29-9504-22e8320ffbd6.png)

The different pipeline modules are supposed to be as independent from each other as possible. They can be done by different solutions. This first base version runs with the following setup:
![Application diagrams-OPMThis Pipeline drawio](https://user-images.githubusercontent.com/46896615/162033661-effa5432-e9ca-4960-a873-4cdfbf17cf02.png)


## OPMthis Structure
This application is structured as the following:

![ModuleView drawio](https://user-images.githubusercontent.com/46896615/161813919-cefa9fed-a7a1-4796-900d-511ce8121a35.png)

The consists of a backend and a frontend. The frontend is only meant to provide an environment to easyly test and evaluate OPM approaches. The backend falls into two parts: Event generation and OPM computing.

## Installation OPMthis
_How to run OPMthis_

## Getting started OPMthis pipeline
_How to setup the overall pipeline with Webflow, GTM and Kafka_

### Examplary event stream
_How to generate an event stream from test data: Adidas mode_
