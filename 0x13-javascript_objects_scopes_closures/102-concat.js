#!/usr/bin/node
/* script that concats 2 files.
    arg 1 = file path of the first source file
    arg 2 = the file path of the second source file
    arg 3 = the file path of the destination */
const files = require('files');

const fArg = fs.readFileSync(process.argv[2]).toString();
const sArg = fs.readFileSync(process.argv[3]).toString();
files.writeFileSync(process.argv[4], fArg + sArg);

