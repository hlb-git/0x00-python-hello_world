#!/bin/bash
#send post request with header variable
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
