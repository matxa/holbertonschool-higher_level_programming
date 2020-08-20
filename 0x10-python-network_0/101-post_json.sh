#!/bin/bash
# post request
echo "\"\"" && curl -s -H "Content-Type: application/json" -d @"$2" "$1"
