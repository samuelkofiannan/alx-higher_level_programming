#!/bin/bash
# Follows a URL for it to respond with "You got me!"
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"
