#!/bin/bash
# post request
curl -s -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X "POST" "$1"
