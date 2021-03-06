#!/usr/bin/node
// lookup how many movies WedgeAntilles is in

const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = [];
    for (let i = 0; i < data.results.length; i++) {
      const res = data.results[i].characters;
      for (let r = 0; r < res.length; r++) {
        if (res[r] === 'https://swapi-api.hbtn.io/api/people/18/' || res[r] === 'http://swapi.co/api/people/18/') {
          characters.push(res[r]);
        }
      }
    }
    console.log(characters.length);
  }
});
