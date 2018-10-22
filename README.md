# kanetix test app


## requirements

download and install the following:

docker - https://www.docker.com/

## setup

let's setup the environment which includes flask, a python web framework (http://flask.pocoo.org/)

run the following commands in terminal:

`cd /kanetix-test/` (navigate to extracted folder)

`docker-compose build` (build docker container)

`docker-compose run --rm --service-ports kanetix-test sh`	(connect to container)

`python app.py` (start flask app)

now visit `http://localhost:8000/` in a browser to view our flask test app.
if everything worked you should see 'hello world!', and can start the test :)

if you have problems with the setup, see if you can figure it out, but if you're stuck, don't stress, contact us

## instructions

1. no rates are being returned for Sonnet (company id = 4), can you determine why and fix? once complete and you're happy with your code, email back the code

2. The endpoint used to get RBC rates (company id = 5) is flakey and only returns rates when it feels like, can you think of a way we can always display a rate?

3. The front end js makes alot of api calls, can you think of a better way to display the required data?

once complete package the code up and send back. include any notes on your thoughts or design considerations
