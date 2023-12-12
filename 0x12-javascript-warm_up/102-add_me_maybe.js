#!/usr/bin/node
/*unction that increments and calls a function
      Prototype: function (number, theFunction)*/
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
