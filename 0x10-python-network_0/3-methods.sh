#!/bin/bash
#Shows allowed verbs at IP
curl -sI "$1" | grep -i "Allow" | awk -F ": " '{print $2}'
