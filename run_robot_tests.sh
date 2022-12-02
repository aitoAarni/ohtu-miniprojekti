#!/bin/bash

# käynnistetään Flask-palvelin taustalle
poetry run python3 src/index.py &

# suoritetaan testit
poetry run robot src/e2e

status=$?


exit $status