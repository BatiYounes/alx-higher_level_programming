#!/usr/bin/node

const x = process.argv[2];

if (isNaN(x) || x === undefined) {
  console.log('Missing number of occurrences');
} else {
  let i = 1;
  while (i <= x) {
    console.log('C is fun');
    i++;
  }
}
