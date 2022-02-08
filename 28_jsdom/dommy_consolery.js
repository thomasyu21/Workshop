/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Raymond Yeung, Thomas Yu
// SoftDev pd1
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08t
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

//
let addItem = function(text) {
  let list = document.getElementById("thelist");
  console.log(list);
  let newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};
console.log(thelist);

let removeItem = function(n) {
  let listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


let red = function() {
  let items = document.getElementsByTagName("li");
  for(let i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


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
// FAC
// GCD
