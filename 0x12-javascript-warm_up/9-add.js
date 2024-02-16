#!/usr/bin/node
const argv = process.argv.slice(2);
add(Number.parseInt(argv[0]), Number.parseInt(argv[1]));
function add (a, b) {
  console.log(a + b);
}
