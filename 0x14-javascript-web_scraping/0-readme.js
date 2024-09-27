#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2]; // The first argument is the file path

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err); // If an error occurred during the reading, print the error object
  } else {
    console.log(data); // Print the content of the file
  }
});
