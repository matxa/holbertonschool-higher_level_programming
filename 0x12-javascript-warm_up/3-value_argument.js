#!/usr/bin/node
// get argv print argv
if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
