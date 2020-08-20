#!/bin/bash
# status code of the response
curl -Is curl -Is "$1" | grep 'HTTP/1.0' | cut -d ' ' -f2
