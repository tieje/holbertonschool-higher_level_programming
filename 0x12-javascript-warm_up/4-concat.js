#!/usr/local/bin/node

import { argv } from 'process';

const printIsArgs = (arr) => {
  let ln = arr.length;
  let first_arg = 'undefined', sec_arg = 'undefined';
  if (ln >= 3) {
    first_arg = arr[2];
  }
  if (ln === 4) {
    sec_arg = arr[3];
  }
  console.log(first_arg + ' is ' + sec_arg);
};

printIsArgs(argv);
