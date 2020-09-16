#!/usr/bin/node
// factorial
let total = 1;
for (let num = 1; num <= parseInt(process.argv[2]); num++) {
  total = total * num;
}
console.log(total);
