#!/usr/bin/node
const printXTimes = (arg) => {
  if (arg.length < 3) {
    console.log('Missing number of occurrences');
  } else {
    for (var i = 0; i < Number(arg[2]); i++) {
      console.log('C is fun');
    }
  }
};

printXTimes(process.argv);
