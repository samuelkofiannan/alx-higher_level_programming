#!/usr/bin/node
// A script that display the status code of a get request

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
