const fs = require("fs");

const readFileLines = (filename) =>
  fs
    .readFileSync(filename)
    .toString("UTF8")
    .split("\n")
    .map((l) => Number(l));

const expenses = readFileLines("inputs/1.txt");

const findAddends = (expenses, sum) => {
  let addends;
  expenses.forEach((e1) => {
    expenses.forEach((e2) => {
      if (e1 + e2 === sum) {
        addends = [e1, e2];
      }
    });
  });
  return addends;
};

const addends = findAddends(expenses, 2020);
console.log(addends[0] * addends[1]);
