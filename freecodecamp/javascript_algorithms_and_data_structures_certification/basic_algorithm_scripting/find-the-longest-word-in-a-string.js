function findLongestWordLength(str) {
  let temp = 0;
  let data = str.split(" ");
  for (let entry = 0; entry < data.length; entry++){
    // console.log(data[entry]);
    if ( data[entry].length > temp){
      temp = data[entry].length;
    }
  }
  return temp;
}

findLongestWordLength("The quick brown fox jumped over the lazy dog");