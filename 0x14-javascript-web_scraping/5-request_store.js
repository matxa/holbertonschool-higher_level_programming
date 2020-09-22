#!/usr/bin/node
// Loripsum

const fs = require('fs');
const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, (err, res, body) => {
  if (!err) {
    fs.writeFile(process.argv[3], body, { flag: 'w', encoding: 'utf8' }, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
