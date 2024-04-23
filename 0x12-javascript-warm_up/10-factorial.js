#!/usr/bin/node
const argv = process.argv.slice(2);
console.log(factorial(Number.parseInt(argv[0])));
function factorial (x) {
  if (x === 0) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}
