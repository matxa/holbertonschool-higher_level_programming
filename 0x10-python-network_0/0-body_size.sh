#!/bin/bash
# get body content size
curl -Is "$1" | grep 'Content-Length' | cut -d ' ' -f2
