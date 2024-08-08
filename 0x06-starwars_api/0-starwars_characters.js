#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

function urlPromise (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (err, res, body) {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

request.get(filmUrl, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const characters = JSON.parse(body).characters;
  const charactersPromises = characters.map(url => urlPromise(url));
  Promise.all(charactersPromises).then(function (results) {
    results.forEach(name => {
      console.log(name);
    });
  });
});
