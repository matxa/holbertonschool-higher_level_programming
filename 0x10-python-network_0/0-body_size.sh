#!/bin/bash
curl -Is $1 | grep 'Content-Length' | cut -d ' ' -f2

