#!/usr/bin/node
// a script that reads and prints the content of a file

const fs = require('fs');
const contents = fs.readFileSync(process.argv[2], 'utf8');
console.log(contents);
