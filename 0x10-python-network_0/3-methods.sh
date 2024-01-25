#!/bin/bash
#print allowed methods on server
curl -sI "$1" | grep 'Allow' | cut ' ' -f 2-
