#!/usr/bin/node
const args = process.argv.slice(2);

const parsedInt = parseInt(args[0]);

if (!isNaN(parsedInt)) {
  console.log(`My number: ${parsedInt}`);
} else {
  console.log('Not a number');
}
