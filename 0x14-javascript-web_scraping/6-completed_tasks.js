#!/usr/bin/node
// get completed

const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, (err, res, body) => {
  if (!err) {
    const data = JSON.parse(body);
    let taksCount = 0;
    const log = {};
    for (let user = 1; user <= 10; user++) {
      for (let i = 0; i < data.length; i++) {
        if (data[i].userId === user) {
          if (data[i].completed) {
            taksCount += 1;
          }
        }
      }
      log[user] = taksCount;
      taksCount = 0;
    }
    console.log(log);
  }
});
