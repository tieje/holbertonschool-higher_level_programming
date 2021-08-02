#!/usr/bin/node

const argv = process.argv;
if (argv[2]) {
  let y = Number(argv[2]);
  if (y && y > 0) {
    for (let i = 0; i < y; i++) {
      console.log('X'.repeat(y));
    }
  } else {
    console.log('Missing size');
  }
}
