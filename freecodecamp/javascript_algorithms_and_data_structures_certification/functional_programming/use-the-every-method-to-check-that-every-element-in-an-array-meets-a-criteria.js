function checkPositive(arr) {
  // Only change code below this line
  //let result = arr.filter(x => x > 0)
  //return result.length === arr.length;
  return  arr.every(function(x){
    return x > 0;
  })
  // Only change code above this line
}
checkPositive([1, 2, 3, -4, 5]);
