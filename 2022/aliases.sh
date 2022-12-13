#!/usr/bin/env bash

alias peehpee="docker run --rm -it -v ${PWD}:/app -w /app php:8.2-alpine php $1"
alias peehpee_shell="docker run --rm -it -v ${PWD}:/app -w /app php:8.2-alpine sh"
