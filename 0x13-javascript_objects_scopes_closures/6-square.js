#!/usr/bin/node
const s = require('./5-square');
module.exports = class Square extends s {
  charPrint (x) {
    if (x !== undefined) {
      for (let r = 0; r < this.height; r++) {
        for (let c = 0; c < this.width; c++) {
          process.stdout.write(x);
        }
        console.log('');
      }
    } else {
      super.print();
    }
  }
};
