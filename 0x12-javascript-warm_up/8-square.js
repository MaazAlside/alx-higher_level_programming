#!/usr/bin/node
if (!process.argv[2] || !parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  const num = parseInt(process.argv[2]);
  for (let i = 0; i < num; i++) {
    let x = '';
    for (let j = 0; j < num; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
