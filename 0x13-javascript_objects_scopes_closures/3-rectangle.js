#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let r = 0; r < this.height; r++) {
      for (let c = 0; c < this.width; c++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }
};
