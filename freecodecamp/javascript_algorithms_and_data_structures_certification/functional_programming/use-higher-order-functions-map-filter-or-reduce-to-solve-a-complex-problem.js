const squareList = (arr) => {
  // Only change code below this line
  return arr.filter(x => x > 0 && Number.isInteger(x)).map(x => x ** 2);
  // Only change code above this line
};

const squaredIntegers = squareList([-3, 4.8, 5, 3, -3.2]);
console.log(squaredIntegers);
console.log(squareList([4, 5.6, -9.8, 3.14, 42, 6, 8.34, -2]));