#!/bin/bash

# käynnistetään Flask-palvelin taustalle
poetry run python3 src/index.py &

# Suoritetaan build
poetry run invoke build & 

# suoritetaan testit
poetry run robot src/tests

status=$?


exit $status