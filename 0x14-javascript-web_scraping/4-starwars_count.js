#!/usr/bin/node
// lookup how many movies WedgeAntilles is in

const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, (err, res, body) => {
  if (!err) {
    const data = JSON.parse(body);
    const characters = [];
    for (let i = 0; i < data.results.length; i++) {
      const WedgeAntilles = data.results[i].characters.find(check => check === 'https://swapi-api.hbtn.io/api/people/18/');
      if (WedgeAntilles) {
        characters.push(WedgeAntilles);
      }
    }
    console.log(characters.length);
  }
});
