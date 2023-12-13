#!/usr/bin/node
/* script that create  class Rectangle that take args w and h
If w or h is equal to 0 or not a positive integer, create an empty object
 Create an instance method called print() that prints the rectangle using the character X */
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;

