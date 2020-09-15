#!/usr/bin/node
// get argv convert to int and print argv number on times

if (parseInt(process.argv[2])) {
  for (let step = 0; step < parseInt(process.argv[2]); step++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
