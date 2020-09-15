#!/usr/bin/node
// get argv
// print process.argv
if (process.argv.length === 1) {
  console.log('No argument');
}
if (process.argv.length === 2) {
  console.log('Argument found');
}
if (process.argv.length > 2) {
  console.log('Arguments found');
}
