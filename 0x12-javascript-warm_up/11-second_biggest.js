#!/usr/bin/node
// factorial
if (!process.argv[2]) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  const array = process.argv.slice(2, process.argv.length);
  array.sort();
  array.pop();
  console.log(Math.max(...array));
}
