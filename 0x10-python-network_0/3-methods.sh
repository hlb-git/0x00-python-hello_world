#!/bin/bash
#print allowed methods on server
curl -sI "$1" | grep 'Allow' | cut -d ' ' -f 2-
