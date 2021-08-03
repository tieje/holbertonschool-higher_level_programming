#!/usr/bin/node
exports.esrever = function (list) {
  const ln = list.length;
  const newList = [];
  for (let i = ln; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
