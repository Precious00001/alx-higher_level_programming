#!/usr/bin/node
const fs = require('fs');

const A = fs.readFileSync(process.argv[2]).toString();
const B = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], A + B);
