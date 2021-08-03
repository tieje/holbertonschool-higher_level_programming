#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const ln = list.length;
  for (let i = 0; i < ln; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
