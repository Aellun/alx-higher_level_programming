#!/usr/bin/node
/* script that prints a square
    arg1 = size(missing size) if be converted to str)
    char x use to print square */

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
