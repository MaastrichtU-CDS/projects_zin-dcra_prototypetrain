# PrototypeTrain
This repository contains the code to demonstrate how to interact with the Station application of Railway.
It contains a simple Master and Station example.

## Folders
The following folders are used by Station to write to and read from the docker application.
The format of the input and output text can be any format and is free to be implemented by the Train creator
The tasks information is a fixed JSON format.
- INPUT_PATH = '/opt/input.txt'
- OUTPUT_PATH = '/opt/output.txt'
- COMPLETED_TASK_PATH = '/opt/completed-client-tasks.json'
- NEW_TASK_PATH = '/opt/new-client-tasks.json'

## Master algorithm
The master algorithm must be triggered to combine information from the different station algorithms.
The completed tasks JSON is always provided (even on the first run) and will contain the in and output of every Station task

## Station algorithm
The station algorithm contains the code that will be run to process the local data.
The result can never be any identifiable data as it is returned to the server/master algorithm.

## Creating your own train
- copy this repository to your own.
- use the StationInterface to read and write output.
- use the simulateMasterAndStation as an example how to debug your algorithm.

## Setting up the container
use these steps to manage a new train container locally

- using your preferred terminal to go to the root of the repository and use the following commands
### build the image
- run "docker build --no-cache -t test_train ."
### start the image
- run "docker run -d -it --name=test_train test_train"
### Enter container for interactive debugging
- docker exec -it test_train /bin/bash
### Copy new version to running container if you make changes
- docker cp ./src/. test_train:/app

## Cleaning up when you are done
### Stop the image
- docker stop test_train
### Remove the image
- docker rm test_train

## Debugging using jupyter
- install anaconda for your OS (https://www.anaconda.com/distribution/)
- run "conda install -c conda-forge jupyterlab" in the anaconda terminal