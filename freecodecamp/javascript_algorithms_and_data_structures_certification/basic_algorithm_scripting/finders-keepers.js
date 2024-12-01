function findElement(arr, func) {
  let num = undefined;
  // console.log(num, arr);
  for(const entry of arr){
    // console.log(entry, func(entry));
    if(func(entry) === true){
      // console.log("num is ", entry);
      return entry;
    }
  }
  return num;
}

findElement([1, 2, 3, 4], num => num % 2 === 0);
