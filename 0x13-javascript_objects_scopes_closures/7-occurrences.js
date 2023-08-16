#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  if (list === undefined || list.length === 0) {
    return;
  }
  let n = 0;
  for (const i of list) {
    if (i === searchElement) {
      n++;
    }
  }
  return n;
};
