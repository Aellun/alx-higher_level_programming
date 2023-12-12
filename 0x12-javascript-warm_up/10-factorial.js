#!/usr/bin/node
/* script that computes and prints a factorial
    Factorial of NaN is 1 */
function factorial (n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 0 || isNaN(n)) {
    return (1);
  }
  return (n * factorial(n - 1));
}
console.log(factorial(Number(process.argv[2])));
