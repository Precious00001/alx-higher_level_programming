#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Define the URL for the Star Wars film API based on the command-line argument
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

// Make an HTTP GET request to fetch film data
request(url, function (error, response, body) {
  // Check if there are no errors in the request
  if (!error) {
    // Parse the film data as JSON and extract the 'characters' array
    const characters = JSON.parse(body).characters;
    
    // Call the 'printCharacters' function to print character names
    printCharacters(characters, 0);
  }
});

// Define a recursive function to print character names from their URLs
function printCharacters(characters, index) {
  // Make an HTTP GET request to fetch character data
  request(characters[index], function (error, response, body) {
    // Check if there are no errors in the request
    if (!error) {
      // Parse the character data as JSON and print the character's name
      console.log(JSON.parse(body).name);

      // Check if there are more characters to print
      if (index + 1 < characters.length) {
        // Recursively call the 'printCharacters' function for the next character
        printCharacters(characters, index + 1);
      }
    }
  });
}

