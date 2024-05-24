#!/usr/bin/node
// A script that reads and prints the content of a file

const fs = require('fs');

if (process.argv.length > 2) {
  fs.readFile(process.argv[2], (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data.toString('utf-8'));
    }
  });
}
