#!/usr/bin/node
// factorial
function SecondLargest (array) {
  array.sort(function (x, y) {
    return x - y;
  });
  const unique = [array[0]];
  const result = [];

  for (let j = 1; j < array.length; j++) {
    if (array[j - 1] !== array[j]) {
      unique.push(array[j]);
    }
  }
  result.push(unique[unique.length - 2]);
  return result.join(',');
}

if (!process.argv[2]) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  const array = process.argv.slice(2, process.argv.length);
  console.log(SecondLargest(array));
}
