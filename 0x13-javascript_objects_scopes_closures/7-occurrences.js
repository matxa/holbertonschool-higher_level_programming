#!/usr/bin/node
// function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  list.forEach((element) => {
    if (element === searchElement) {
      counter++;
    }
  });
  return counter;
};
