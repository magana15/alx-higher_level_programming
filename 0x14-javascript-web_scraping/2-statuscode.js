#!/usr/bin/node
const process = require('process');
const request = require('request');

// take the first argument as the URL to request (GET)
const url = process.argv[2];

request(url, function (error, response) {
  if (error == null) {
    // display the status code of the GET request.
    console.log(`code: ${response.statusCode}`);
  }
});
