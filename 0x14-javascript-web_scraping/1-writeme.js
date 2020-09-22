#!/usr/bin/node
// write to file

const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], { flag: 'w', encoding: 'utf8' }, (err) => {
  if (err) {
    console.log(err);
  }
});
