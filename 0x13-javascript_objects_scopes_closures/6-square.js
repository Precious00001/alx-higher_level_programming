#!/usr/bin/node
const SquareD = require('./5-rectangle.js');
module.exports = class Square extends SquareD {
  charPrint (c) {
    if (c === undefined) {
      return this.print();
    } else {
      let D = '';
      for (let q = 0; q < this.width; q++) {
        D += c;
      }
      for (let q = 0; q < this.height; q++) {
        console.log(D);
      }
    }
  }
};
