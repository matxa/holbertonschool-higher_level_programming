#!/bin/bash
# Get the body (byte)size using curl

curl -s $1 | wc -c
