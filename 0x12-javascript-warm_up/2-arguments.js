#!/usr/bin/node
import { argv } from 'process';

const ArgsFound = (arg) => {
  arg.length > 2 ? console.log('Argument found') : console.log('No argument');
};

ArgsFound(argv);
