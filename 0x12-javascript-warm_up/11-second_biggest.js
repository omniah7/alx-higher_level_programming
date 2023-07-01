#!/usr/bin/node
const argv = new Int16Array(process.argv.slice(2));
const args = argv.length;
if (args <= 1) {
  console.log(0);
} else {
  console.log(argv.sort()[args - 2]);
}
