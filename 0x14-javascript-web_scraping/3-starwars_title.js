#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the episode number from the command line arguments
const episodeNum = process.argv[2];

// Define the URL of the Star Wars API
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

// Make an HTTP GET request to the API using the specified episode number
request(API_URL + episodeNum, function (err, response, body) {
  // Check for errors in the request
  if (err) {
    console.log(err);
  } 
  // Check if the response status code is 200 (OK)
  else if (response.statusCode === 200) {
    // Parse the response body as JSON
    const responseJSON = JSON.parse(body);
    
    // Output the title of the film from the JSON response
    console.log(responseJSON.title);
  } 
  // Handle other response status codes (e.g., error)
  else {
    console.log('Error code: ' + response.statusCode);
  }
});
