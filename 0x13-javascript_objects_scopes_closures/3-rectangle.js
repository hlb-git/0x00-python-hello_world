#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    while (this.height) {
      console.log('x'.repeat(this.width));
      this.height--;
    }
  }
}

module.exports = Rectangle;
