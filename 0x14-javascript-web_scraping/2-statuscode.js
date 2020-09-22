#!/usr/bin/node
// make a request and get status code

const request = require('request');

request.get(process.argv[2]).on('response', (response) => {
  console.log('code: ' + response.statusCode);
});
