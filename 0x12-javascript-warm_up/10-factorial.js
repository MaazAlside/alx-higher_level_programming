#!/usr/bin/node
if (!process.argv[2] || !parseInt(process.argv[2])) {
  console.log(1);
} else {
  function factorial (a) {
    if (a === 1) {
      return (1);
    }
    return (a * factorial(a - 1));
  }
  console.log(factorial(parseInt(process.argv[2])));
}
