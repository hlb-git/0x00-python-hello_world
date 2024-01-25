#!/bin/bash
#send post request with header variable
curl -s -o /dev/null -w "%{http_code}" "$1"
