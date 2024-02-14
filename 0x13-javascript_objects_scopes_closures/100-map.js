#!/usr/bin/node
const { list } = require('./100-data');
const newArray = list.map((x, i) => x * i);
console.log(list);
console.log(newArray);
