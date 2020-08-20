#!/bin/bash
# post request
echo "\"\"" && curl -H "Content-Type: application/json" -d @"$2" "$1"
