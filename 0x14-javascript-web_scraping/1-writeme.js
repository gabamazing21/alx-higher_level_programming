#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2]; // The first argument is the file path
const content = process.argv[3];  // The second argument is the string to write

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.log(err); // If an error occurred during the writing, print the error object
  }
});

