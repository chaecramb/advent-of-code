const fs = require("fs");

const readFileLines = (filename) =>
  fs
    .readFileSync(filename)
    .toString("UTF8")
    .split("\n")
    .map((l) => Number(l));

const expenses = readFileLines("inputs/1.txt");

const findAddends = (array, targetSum) => {
  let addends;
  array.forEach((n1) => {
    array.forEach((n2) => {
      if (n1 + n2 === targetSum) {
        addends = [n1, n2];
      }
    });
  });
  return addends;
};

const addends = findAddends(expenses, 2020);
console.log(addends[0] * addends[1]);

const findPairsWithSum = (array, targetSum) => {
  const pairs = [];
  const seen = new Set();

  array.forEach((n) => {
    const complement = targetSum - n;
    if (seen.has(complement)) {
      pairs.push([n, complement]);
    }
    seen.add(n);
  });

  return pairs;
};

const addends2 = findPairsWithSum(expenses, 2020);
console.log(addends2);
console.log(addends2[0][0] * addends2[0][1]);
