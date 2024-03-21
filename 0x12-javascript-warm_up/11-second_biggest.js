#!/usr/bin/node

function secondBiggest(arr) {
  if (arr.length <= 2) {
    return 0;
  }
  const sortedArr = arr.sort((a, b) => b - a);
  return sortedArr[1];
}

const args = process.argv.slice(2).map(Number);

console.log(secondBiggest(args));
