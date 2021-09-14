#!/usr/bin/node
// #!/usr/local/bin/node
// Reads and prints the content of the file

const fs = require('fs');
const wF = process.argv[2];
const wString = process.argv[3];
const writeOptions = {
  encoding: 'utf8',
  flag: 'w'
};
fs.writeFile(wF, wString, writeOptions, (err) => {
  if (err) {
    return err;
  }
});
