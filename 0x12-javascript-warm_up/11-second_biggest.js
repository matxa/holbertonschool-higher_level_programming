#!/usr/bin/node
// factorial
if (!process.argv[2] || process.argv.length < 4) {
  console.log(0);
} else {
  const array = process.argv.slice(2, process.argv.length);
  array.sort();
  array.pop();
  console.log(Math.max(...array));
}
