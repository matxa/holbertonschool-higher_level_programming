#!/usr/bin/node
// get argv convert to int and print argv number on times
function add (a, b) {
  console.log(a + b);
}

add(parseInt(process.argv[2]), parseInt(process.argv[3]));
