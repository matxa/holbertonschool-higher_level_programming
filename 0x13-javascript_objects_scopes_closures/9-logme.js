#!/usr/bin/node
// print num of args printed

const array = [];
exports.logMe = function (item) {
  array.push(item);
  const index = array.indexOf(item);
  console.log(index + ': ' + array[index]);
};
