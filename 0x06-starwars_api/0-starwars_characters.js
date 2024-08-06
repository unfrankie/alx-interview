#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;
request(apiUrl, async function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;
  const getCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
  };

  const characterPromises = characters.map(url => getCharacterName(url));
  try {
    const characterNames = await Promise.all(characterPromises);

    characterNames.forEach(name => console.log(name));
  } catch (err) {
    console.error('Error:', err);
  }
});
