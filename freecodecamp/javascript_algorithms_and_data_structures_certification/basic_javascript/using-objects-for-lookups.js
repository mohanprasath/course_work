// Setup
function phoneticLookup(val) {
  var result = "";

  // Only change code below this line
  var temp = {
    "alpha":"Adams",
    "bravo":"Boston",
    "charlie":"Chicago",
    "delta":"Denver",
    "echo":"Easy",
    "foxtrot":"Frank",
    }
    result = temp[val];

  // Only change code above this line
  return result;
}

phoneticLookup("charlie");
