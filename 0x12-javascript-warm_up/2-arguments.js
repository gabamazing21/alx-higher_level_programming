#!/usr/bin/node
const argv = process.argv.slice(2);
if (argv.length === 1) {
  console.log('Argument found');
} else if (argv.length === 0) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
