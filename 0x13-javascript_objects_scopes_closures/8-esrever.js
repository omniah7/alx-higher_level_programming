#!/usr/bin/node
exports.esrever = function (list) {
  if (list === undefined || list.length === 0) {
    return;
  }
  const rev = [];
  for (let i = list.length - 1; i >= 0; i--) {
    rev.push(list[i]);
  }
  return rev;
};
