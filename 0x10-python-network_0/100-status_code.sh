#!/bin/bash
# Sends a request to '$1' and displays only the status code
curl -so /dev/null -w "%{http_code}" "$1"
