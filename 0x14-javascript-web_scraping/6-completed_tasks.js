#!/usr/bin/node
// get completed

const request = require('request');

request('https://jsonplaceholder.typicode.com/users', (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const userAmount = JSON.parse(body).length;
    request(process.argv[2], (err, res, body) => {
      if (!err && res.statusCode === 200) {
        const data = JSON.parse(body);
        let taksCount = 0;
        const log = {};
        for (let user = 1; user <= userAmount; user++) {
          for (let i = 0; i < data.length; i++) {
            if (data[i].userId === user) {
              if (data[i].completed) {
                taksCount += 1;
                log[user] = taksCount;
              }
            }
          }
          taksCount = 0;
        }
        console.log(log);
      }
    });
  }
});
