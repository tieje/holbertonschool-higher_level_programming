#!/usr/bin/node

function getFactorio (a) {
  const n = Number(a);
  if (isNaN(n) || n === 1) {
    return 1;
  }
  return n * getFactorio(n - 1);
}
console.log(getFactorio(process.argv[2]));
