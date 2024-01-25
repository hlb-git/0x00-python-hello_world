#!/bin/bash
#print size of the body to the stdout
curl -w '%{size_download}\n' -s "$1" | tail -1
