#!/usr/bin/node
const arg = process.argv;
if (arg.length < 3) {
  console.log('Missing number of occurrences');
} else {
  if (Number(arg[2] > 0)) {
    for (let i = 0; i < Number(arg[2]); i++) {
      console.log('C is fun');
    }
  }
}
