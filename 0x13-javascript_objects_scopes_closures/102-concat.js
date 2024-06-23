#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <fileA> <fileB> <fileC>');
  process.exit(1);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

try {
  const dataA = fs.readFileSync(fileA, 'utf8');
  const dataB = fs.readFileSync(fileB, 'utf8');
  fs.writeFileSync(fileC, dataA + dataB);
} catch (err) {
  console.error('Error:', err.message);
  process.exit(1);
}
