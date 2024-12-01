function countOnline(usersObj) {
  // Only change code below this line
  let count = 0;
  for(let user in usersObj){
    if(usersObj[user]["online"]){
      count += 1;
    }
  }
  console.log(count);
  return count;
  // Only change code above this line
}
countOnline({ Alan: { online: true }, Jeff: { online: false }, Sarah: { online: true } })