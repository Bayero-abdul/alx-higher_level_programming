#!/usr/bin/node
const Square0 = require('./5-square.js');

module.exports = class Square extends Square0 {
  charPrint (c) {
    if (c) {
      const w = this.width;
      const h = this.height;
      for (let i = 0; i < h; i++) {
        console.log(c.repeat(w));
      }
    } else {
      this.print();
    }
  }
};
