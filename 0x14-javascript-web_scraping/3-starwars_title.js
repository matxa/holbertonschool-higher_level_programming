#!/usr/bin/node

const request = require('request');

const options = {
  url: `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  method: 'GET'
};

request(options, (err, res, body) => {
  if (!err) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
