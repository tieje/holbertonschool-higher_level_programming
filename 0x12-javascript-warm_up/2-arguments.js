#!/usr/bin/node

const ArgsFound = (arg) => {
  if (arg.length === 2) {
    console.log('No argument');
  } else if (arg.length === 3) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
};

ArgsFound(process.argv);
