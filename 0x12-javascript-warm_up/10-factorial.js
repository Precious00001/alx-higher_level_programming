#!/usr/bin/node
function factorial (q) {
  if (q < 0) {
    return (-1);
  }
  if (q === 0 || isNaN(q)) {
    return (1);
  }
  return (q * factorial(q - 1));
}

console.log(factorial(Number(process.argv[2])));
