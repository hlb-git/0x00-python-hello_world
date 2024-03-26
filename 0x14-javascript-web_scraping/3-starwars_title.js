#!/usr/bin/node
// script to fetch star wars api data usin request library

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    } else {
    const output = JSON.parse(body);
    console.log(output.title);
  }
});
