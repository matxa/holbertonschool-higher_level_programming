#!/usr/bin/node

const request = require('request');

const options = {
  url: `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  method: 'GET'
};

request(options, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body).characters;
    for (let i = 0; i < data.length; i++) {
      request(data[i], (err, res, body) => {
        if (!err && res.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
