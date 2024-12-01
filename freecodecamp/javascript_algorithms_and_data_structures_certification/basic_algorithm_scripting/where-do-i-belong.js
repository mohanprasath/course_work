function getIndexToIns(arr, num) {
  let result = arr.filter(x => x < num);

    return result.length;
  //}
}

getIndexToIns([40, 60], 50);
