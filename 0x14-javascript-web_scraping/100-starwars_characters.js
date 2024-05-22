const request = require('request');

// Extract movie ID from command line arguments
const movieId = process.argv[2];

// Construct the URL
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
        // Print the characters
        console.log(`Characters in "${movie.title}":`);
        movie.characters.forEach(characterUrl => {
            request.get(characterUrl, (err, res, charBody) => {
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
            });
        });
    } catch (parseError) {
        console.error('Error parsing response:', parseError);
    }
});

