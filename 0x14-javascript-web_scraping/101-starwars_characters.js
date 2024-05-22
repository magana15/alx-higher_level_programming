#!/usr/bin/node
const request = require('request');

// Check if the movie ID argument is provided
if (process.argv.length !== 3) {
    console.error('Usage: node script.js <movie_id>');
    process.exit(1);
}

// Extract movie ID from command line arguments
const movieId = process.argv[2];

// Construct the URL for the movie
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request.get(url, (error, response, body) => {
    if (error) {
        console.error('Error making GET request:', error);
        return;
    }
    if (response.statusCode !== 200) {
        console.error('Failed to retrieve movie information. Status code:', response.statusCode);
        return;
    }
    try {
        const movie = JSON.parse(body);
        const characterUrls = movie.characters;

        // Function to fetch and print character names in order
        const fetchCharacterNames = (urls, index = 0) => {
            if (index >= urls.length) {
                return;
            }
            request.get(urls[index], (err, res, charBody) => {
                if (err) {
                    console.error('Error making GET request for character:', err);
                    return;
                }
                if (res.statusCode !== 200) {
                    console.error('Failed to retrieve character information. Status code:', res.statusCode);
                    return;
                }
                const character = JSON.parse(charBody);
                console.log(character.name);
                fetchCharacterNames(urls, index + 1);
            });
        };

        // Start fetching character names
        fetchCharacterNames(characterUrls);
    } catch (parseError) {
        console.error('Error parsing response:', parseError);
    }
});

