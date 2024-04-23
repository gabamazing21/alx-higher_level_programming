#!/usr/bin/node
const argv = process.argv.slice(2);
if (argv.length === 0) {
  console.log(1);
} else {
  console.log(factorial(Number.parseInt(argv[0])));
}
function factorial (x) {
  if (x === 0) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}
