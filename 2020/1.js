const fs = require("fs");

const readFileLines = (filename) =>
  fs
    .readFileSync(filename)
    .toString("UTF8")
    .split("\n")
    .map((l) => Number(l));

const expenses = readFileLines("inputs/1.txt");

const findAddends = (array, sum) => {
  let addends;
  array.forEach((n1) => {
    array.forEach((n2) => {
      if (n1 + n2 === sum) {
        addends = [n1, n2];
      }
    });
  });
  return addends;
};

const addends = findAddends(expenses, 2020);
console.log(addends[0] * addends[1]);
