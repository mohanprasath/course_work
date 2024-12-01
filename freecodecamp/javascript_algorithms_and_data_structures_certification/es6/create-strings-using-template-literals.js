const result = {
  success: ["max-length", "no-amd", "prefer-arrow-functions"],
  failure: ["no-var", "var-on-top", "linebreak"],
  skipped: ["id-blacklist", "no-dup-keys"]
};
function makeList(arr) {
  "use strict";

  // Only change code below this line
  let resultDisplayArray = [];
  for( let i = 0; i < result.failure.length; i++){
    resultDisplayArray.push(`<li class="text-warning">${result.failure[i]}</li>`)
  }
  // Only change code above this line

  return resultDisplayArray;
}

const resultDisplayArray = makeList(result.failure);
