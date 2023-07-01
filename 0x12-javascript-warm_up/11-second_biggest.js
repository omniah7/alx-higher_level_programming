#!/usr/bin/node
const argv =new Int16Array(process.argv.slice(2));
const args = argv.length;
if (args <= 1) {
  console.log(0);
} else {
  const ls = argv.sort();
  console.log(ls[args - 2]);
}
