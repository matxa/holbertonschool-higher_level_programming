#!/usr/bin/node
// make a request and get status code

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    console.log('code: ', response.statusCode);
  }
});
