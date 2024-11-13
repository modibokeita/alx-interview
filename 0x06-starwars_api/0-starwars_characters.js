#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Validate that the Movie ID argument is provided
if (!movieId) {
  console.error('Please provide a Movie ID as an argument');
  process.exit(1);
}

request(apiUrl, (err, res, body) => {
  if (err) return console.error(err);
  const data = JSON.parse(body);

  // Check if the characters list exists in the response
  if (!data.characters) return console.error('No characters found for this movie.');

  // Fetch and display each character's name
  const characterUrls = data.characters;
  let count = 0;

  // Helper function to display characters in the same order as they appear in the array
  function fetchCharacter(index) {
    if (index >= characterUrls.length) return;

    request(characterUrls[index], (err, res, body) => {
      if (err) return console.error(err);
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      fetchCharacter(index + 1); // Fetch the next character
    });
  }

  fetchCharacter(0); // Start fetching from the first character in the list
});

