#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const newList = [];
  for (let i = 0; i < list.length; i++) {
    newList.unshift(list[i]);
  }
  return newList;
};
