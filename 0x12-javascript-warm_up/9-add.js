#!/usr/bin/node
if (!process.argv[2] || !parseInt(process.argv[2]) || !process.argv[3]) {
  console.log('NaN');
} else {
  function add (a, b) {
    console.log(parseInt(a) + parseInt(b));
  }
  add(parseInt(process.argv[2]), parseInt(process.argv[3]));
}
