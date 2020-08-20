#!/bin/bash
# post request
curl -H "Content-Type: application/json" -d @"$2" "$1"
