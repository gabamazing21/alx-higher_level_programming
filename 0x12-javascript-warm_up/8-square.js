#!/usr/bin/node
const argv = process.argv.slice(2);
if (Number.parseInt(argv[0])) {
  for (let i = 0; i < argv[0]; i++) {
    let squares = '';
    for (let j = 0; j < argv[0]; j++) {
      squares = squares + 'X';
    }
    console.log(squares);
  }
} else {
  console.log('Missing size');
}
