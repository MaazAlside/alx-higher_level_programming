#!/usr/bin/node
const _Square = require('./5-square');
class Square extends _Square {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let sympol = '';
        for (let j = 0; j < this.width; j++) {
          sympol += c;
        }
        console.log(sympol);
      }
    }
  }
}

module.exports = Square;
