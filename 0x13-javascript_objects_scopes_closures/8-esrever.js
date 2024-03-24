#!/usr/bin/node

exports.esrever = function (list) {
  let i = list.length - 1;
  let j = 0;

  while ((i - j) > 0) {
    const temp = list[i];
    list[i] = list[j];
    list[j] = temp;
    j++;
    i--;
  }

  return list;
};
