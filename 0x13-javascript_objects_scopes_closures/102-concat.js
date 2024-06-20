#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

// Extract file paths from command-line arguments
const [,, fileA, fileB, fileC] = process.argv;

try {
  // Read the contents of fileA and fileB
  const contentA = fs.readFileSync(fileA, 'utf8').trim();
  const contentB = fs.readFileSync(fileB, 'utf8').trim();

  // Concatenate the contents with a newline in between
  const concatenatedContent = `${contentA}\n${contentB}\n`;

  // Write the concatenated content to fileC
  fs.writeFileSync(fileC, concatenatedContent);

  console.log(`Concatenated ${fileA} and ${fileB} into ${fileC}`);
} catch (error) {
  console.error('Error:', error.message);
  process.exit(1);
}
