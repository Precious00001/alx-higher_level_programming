#!/bin/bash
# send a post a requst with json file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
