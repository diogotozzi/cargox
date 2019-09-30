# CargoX Test Code

This is the project described at `Exercise.md`

It receives a small batch commands in TXT format file from Stdin.

It reads every command, line by line, validates each one against MissionControl() and Plateau(), and
if validation passes, the movement is committed at Rover().

The result of each command is shown at the terminal as a TXT format,
according to the `Exercise.md` requirement.

## Software Architecture
I decide to use a *Manager* entity, called MissionControl() for Rover() interactions.

It allows the developer to call simple commands, abstracting Rover()'s and Plateau()'s more complex
configurations.

I also used the latest *Python 3* programming language for this test, as Python is one
of the cleanest and easiest to read languages available nowadays.

## Running it locally

#### 1 - Build the Docker image
`docker-compose build`

#### 2- Execute locally
`docker-compose run app python3 main.py < input.txt`

## Running unit tests
`docker-compose run app python3 -m unittest discover`
