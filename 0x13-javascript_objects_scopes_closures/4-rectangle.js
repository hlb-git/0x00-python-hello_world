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
      console.log('X'.repeat(this.width));
      this.height--;
    }
  }

  rotate () {
	const tmp = this.width;
	this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

}

module.exports = Rectangle;
