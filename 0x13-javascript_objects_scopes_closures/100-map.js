#!/usr/bin/node
// script that imports an array and computes a new array

const data = require('./100-data').list;

const newList = data.map((item) => {
  return item * data.indexOf(item);
});

console.log(data);
console.log(newList);
