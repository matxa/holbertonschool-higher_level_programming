#!/usr/bin/node
// factorial
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const array = process.argv.slice(2, process.argv.length);
  const newArray = [];
  for (let step = 0; step < array.length; step++) {
    newArray.push(parseInt(array[step]));
  }
  newArray.sort();
  console.log(newArray[newArray.length - 2]);
}
