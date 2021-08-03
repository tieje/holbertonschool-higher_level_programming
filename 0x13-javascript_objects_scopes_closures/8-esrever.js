#!/usr/local/bin/node
exports.esrever = function (list) {
  let ln = list.length;
  let new_list = [];
  for (let i = ln; i >= 0; i--) {
    new_list.push(list[i]);
  }
  return new_list;
};
