#!/usr/bin/node
const argv = process.argv.slice(2);
if (Number.parseInt(argv[0])) {
  console.log(`My number: ${Number.parseInt(argv[0])}`);
} else {
  console.log('Not a number');
}
