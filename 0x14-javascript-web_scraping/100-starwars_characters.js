#!/usr/bin/node

const rqst = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
rqst.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const i of dd) {
    rqst.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const data5 = JSON.parse(body1);
      console.log(data5.name);
    });
  }
});
