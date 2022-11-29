#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w) {
      this.width = w;
    }
    if (h) {
      this.height = h;
    }
  }
};
