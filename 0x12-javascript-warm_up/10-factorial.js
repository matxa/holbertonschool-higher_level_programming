#!/usr/bin/node
// factorial
function factorial (num) {
  if (num === 0 || !num) {
    return 1;
  }
  return num * factorial(num - 1);
}

console.log(factorial(parseInt(process.argv[2])));
