#!/usr/bin/node
// a script that reads and prints the content of a file

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (!err) {
    console.log(data);
  } else {
    console.log(err);
  }
});
