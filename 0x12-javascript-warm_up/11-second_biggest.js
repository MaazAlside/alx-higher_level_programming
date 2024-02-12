#!/usr/bin/node

if (!process.argv[2] || parseInt(process.argv[2]) === 1) {
  console.log(0);
} else {
  let firstBiggest = parseInt(process.argv[2]);
  let secondBiggest = 0;

  for (let i = 2; i < process.argv.length; i++) {
    const currentNumber = parseInt(process.argv[i]);

    if (!isNaN(currentNumber)) {
      if (currentNumber > firstBiggest) {
        secondBiggest = firstBiggest;
        firstBiggest = currentNumber;
      } else if (currentNumber > secondBiggest) {
        secondBiggest = currentNumber;
      }
    }
  }

  console.log(secondBiggest);
}
