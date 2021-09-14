#!/usr/local/bin/node
// #!/usr/bin/node
// Reads and prints the content of the file

const fs = require('fs');
const readThisFile = process.argv[2];
fs.readFile(readThisFile, 'utf8', (err, data) => {
  if (err) return (console.log(err));
  console.log(data);
});
/*
const strs = 'C is super fun!'
const writeOptions = {
  encoding: 'utf8',
  flag: 'w'
}
fs.writeFile(editFile, strs, writeOptions, (err) => {
  if (err) {
    return err
  }
})
const readOptions = {
  encoding: 'utf8',
  flag: 'r'
}
fs.readFile(editFile, readOptions, (err, data) => {
  if (err) {
    return err
  }
  console.log(data)
})
*/
