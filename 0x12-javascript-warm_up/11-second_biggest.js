#!/usr/bin/node

function secondLargestInteger (...arrayOfNumbers) {
  let firstLargest = -Infinity;
  let secondLargest = -Infinity;

  for (let i = 0; i < arrayOfNumbers.length; i++) {
    if (arrayOfNumbers[i] > firstLargest) {
      secondLargest = firstLargest;
      firstLargest = arrayOfNumbers[i];
    } else if (arrayOfNumbers[i] > secondLargest && arrayOfNumbers[i] < firstLargest) {
      secondLargest = arrayOfNumbers[i];
    }
  }

  return secondLargest;
}

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(secondLargestInteger.apply(this, process.argv.slice(2).map(Number)));
}
