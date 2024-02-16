#!/usr/bin/node
const argv = process.argv.slice(2);
if (Number.parseInt(argv[0])) {
  for (let i = 0; i < argv[0]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
