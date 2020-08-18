#!/bin/bash
# display allow
curl -Is curl -Is "$1" | grep 'Allow' | cut -d ' ' -f2-
