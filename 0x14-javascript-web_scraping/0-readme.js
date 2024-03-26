#!/usr/bin/node
// script to read and print file content passed as argument

const args = process.argv;

const fs = require('fs');

fs.readFile(`${args[2]}`, 'utf8', (err, data) => {
  if (err) { console.log(err); } else { console.log(data); }
});
