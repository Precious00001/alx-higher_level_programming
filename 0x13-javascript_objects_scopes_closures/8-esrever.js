#!/usr/bin/node
exports.esrever = function (list) {
  const newAra = [];
  for (let q = list.length - 1; q >= 0; q--) {
    newAra.push(list[q]);
  }
  return newAra;
};
