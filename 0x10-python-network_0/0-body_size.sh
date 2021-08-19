#!/usr/bin/env bash
# Get the body size of the http response
curl -sI "$1"| grep Content-Length | awk '{print $2}'
