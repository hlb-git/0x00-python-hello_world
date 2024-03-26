#!/usr/bin/node
// script to fetch api data usin request library

const request = require('request');
const URL = process.argv[2];
request.get(URL, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:' + ' ' + response.statusCode);
  }
});
