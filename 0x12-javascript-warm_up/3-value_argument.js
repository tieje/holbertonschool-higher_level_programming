#!/usr/local/bin/node

import { argv } from 'process';

argv.length > 2 ? console.log(argv[2]) : console.log('No argument');
