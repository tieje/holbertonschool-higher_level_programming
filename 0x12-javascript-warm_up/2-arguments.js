#!/usr/bin/node
import { argv } from 'process';

const ArgsFound = (arg) => {
  if (arg.length === 3) {
    console.log('Argument found');
  } else if (arg.length > 3) {
    console.log('Arguments found');
  } else {
    console.log('No argument');
  }
};

ArgsFound(argv);
