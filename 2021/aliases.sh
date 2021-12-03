#!/usr/bin/env bash

# make sure you are in 2021 workdir, I am lazy

alias build="docker build -t goland ."
alias go="docker run --rm -it -v ${PWD}:/app -w /app goland go run $1"
