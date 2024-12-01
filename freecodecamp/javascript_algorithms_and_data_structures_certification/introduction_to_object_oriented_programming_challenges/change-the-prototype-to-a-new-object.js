function Dog(name) {
  this.name = name;
}

Dog.prototype = {
  // Only change code below this line
  numLegs:4,
  eat: function(){
    console.log("Dog Eats");
  },
  describe: function(){
    console.log("I am " + this.name);
  }
};
