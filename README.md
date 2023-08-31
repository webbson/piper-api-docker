# piper-api-docker

Wraps the [Piper TTS](https://github.com/rhasspy/piper) in a docker container with a webserver

Make a GET request with query parameters:

- text: text to be spoken
- model: voice to use find the names [here](https://rhasspy.github.io/piper-samples/)

You will get a response with the file name of the generated wav file, which you then can serve with a webserver of your choice.

# Todo:

- [ ] Old file purger
- [ ] Fix datadir and download dir
