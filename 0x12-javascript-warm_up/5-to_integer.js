#!/usr/local/bin/node

import { argv } from 'process';

const convertToNumber = (arr) => {
  let p_number = false;
  if (arr.length == 3) {
    p_number = Number(arr[2]);
  }
  if (!p_number) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + p_number);
  }
};

convertToNumber(argv);
