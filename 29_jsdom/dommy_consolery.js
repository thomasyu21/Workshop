// Thomas Yu, Han Zhang
// SoftDev pd1
// K29 -- DOMfoolery++
// 2022-02-09w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-J in Firefox to reveal console)
console.log("AYO");
//Prints AYO in the console

let i = "hello";
console.log(i);
let j = 20;
console.log(j);
//Just variables we can print out in the console

//assign an anonymous fxn to a var
//Sets j to 30 and then adds whatever x is to j.
//x can be positive or negative. If there is not x given the function returns NaN.
//f(j) returns 50 -> The local j value (30) + the global j value (20)
//f(i) joins the two into a string -> "30hello"
let f = function(x) {
  let j=30;
  return j+x;
};


//instantiate an object (dictionary)
//Recognizes objects ( {} ) as well as arrays ( [] )
//o.<key> outputs the value associated. Works with functions (o.func(10) will return 40)
//Highlights text and numbers when they are values -> Text in pink with "" and numbers in green.
//Has prototype in the tree. What does it do? What does it mean?
let o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };

//Adds a new element to the list on the HTML file
//addItem("item 8") -> "9. item 8" shows up on the site
//returns undefined in the console when the function is ran
//addItem() adds undefined
//addItem("") adds and empty entry to the list
//Numbers will automatically get turned into strings
//Added values on the page don't have class=""
let addItem = function(text) {
  let list = document.getElementById("thelist"); //Gets every element in the list named "thelist" from the HTML file
  let newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

//n is the index of the list for the item you want to remove
//returns undefined in the console
//n needs to be a number within bounds
//Will return TypeError: listitems[n] is undefined when n is out of bounds
//works with items that have been added to the list using addItem(text)
let removeItem = function(n) {
  let listitems = document.getElementsByTagName('li'); //Get all the objects with the tag "li"
  listitems[n].remove();
};

//Makes the text color of the list red
//Only changes the color of the list elements that do not already have a class -> those stay the same color
//Items added afterwards are in black
let red = function() {
  let items = document.getElementsByTagName("li");
  for(let i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};

//Alternates the colors of the items in the list (between red and blue)
//Doesn't affect those that already have a class declared in the HTML file
//Will override red(), but the opposite does not happen
//Items added afterwards are unaffected
let stripe = function() {
  let items = document.getElementsByTagName("li");
  for(let i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
let fib = function(n) {
     if (n <= 1){
	return n;
     }else{
	return fib(n-1) + fib(n-2);
     }
}

// FACT
let fact = function(n) {
     if (n === 0){
        return 1;
     }else{
        return (n * (fact (n - 1)));
     }
}

// GCD
let gcd = function(a,b) {
    if (a < 0){
      return gcd(0-a, b);
    }
    if (b < 0){
      return gcd(a, 0-b);
    }
    if (a > b){
      return gcd(b, a);
    }
    if (a === 0 || b === 0){
      return 0;
    }
    if (b%a === 0){
      return a;
    }else{
      return gcd(a, b%a);
    }
}

let fibButton = document.getElementById("fib");
fibButton.addEventListener('click', event => {
  let n = document.getElementById("fibInput").value;
  let ans = document.getElementById("fibOutput");
  ans.innerText = "= " + fib(n);
});

let factButton = document.getElementById("fact");
factButton.addEventListener('click', event => {
  let n = document.getElementById("factInput").value;
  let ans = document.getElementById("factOutput");
  ans.innerText = "= " + fact(n);
});

let gcdButton = document.getElementById("gcd");
gcdButton.addEventListener('click', event => {
  let a = document.getElementById("gcdInput1").value;
  let b = document.getElementById("gcdInput2").value;
  let ans = document.getElementById("gcdOutput");
  ans.innerText = "= " + gcd(a, b);
});
