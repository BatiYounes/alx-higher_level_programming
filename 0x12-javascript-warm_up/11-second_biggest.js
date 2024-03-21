#!/usr/bin/node

function secondBiggest (arr) {
  if (arr.length <= 2) {
    return 0;
  }
  arr.sort((a, b) => b - a);
  return arr[1];
}

const args = process.argv.slice(2).map(Number);

console.log(secondBiggest(args));
