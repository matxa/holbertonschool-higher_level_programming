#!/bin/bash
# post request
curl "$1" -s -X "POST" -H "Content-Type: application/json" -d @"$2"
