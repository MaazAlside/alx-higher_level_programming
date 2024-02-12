#!/usr/bin/node
if (!process.argv[2] || parseInt(process.argv[2] === 1)) {
  console.log(0);
} else {
  let firstBiggest = parseInt(process.argv[2]);
  let secondBiggest = 0;
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > firstBiggest) {
      secondBiggest = firstBiggest;
      firstBiggest = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) > secondBiggest) {
      secondBiggest = parseInt(process.argv[i]);
    }
  }
  console.log(secondBiggest);
}
