// David Chong, Thomas Yu
// SoftDev pd1
// K32 -- More Moving Parts
// 2022-02-17

// model for HTML5 canvas-based animation


//access canvas and buttons via DOM
var c = document.getElementById("playground"); // GET CANVAS
var dotButton = document.getElementById("buttonCircle"); // GET DOT BUTTON
var stopButton = document.getElementById("buttonStop"); // GET STOP BUTTON
let dvdButton = document.getElementById("buttonDVD");

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d"); // YOUR CODE HERE

//set fill color to team color
ctx.fillStyle = "green" // YOUR CODE HERE

var requestID;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
  console.log("clear invoked...")
  ctx.clearRect(0, 0, c.width, c.height);
  // YOUR CODE HERE
};


var radius = 0;
var growing = true;


//var drawDot = function() {
var drawDot = () => {
  console.log("drawDot invoked...")
  console.log(requestID);
  
  
  clear();
  if (radius > 249){
    growing = false;
  }else if (radius < 1){
    growing = true;
  }
  
  if (growing === true){
    radius+=1;
  }else{
    radius-=1;
  }
  ctx.strokeStyle = "black";
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.arc(c.width/2, c.height/2, radius, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.fill();
  
  if (requestID) {
    window.cancelAnimationFrame(requestID);
  }
  requestID = window.requestAnimationFrame(drawDot);
  
};

let dvdScreensaver = () => {
  console.log(requestID);
  let image = new Image(60, 40);
  image.src = 'logo_dvd.jpg';
  ctx.drawImage(image, 0, 0);
  if (requestID) {
    window.cancelAnimationFrame(requestID);
  }
  requestID = window.requestAnimationFrame(dvdScreensaver);
};

//var stopIt = function() {
var stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );

  window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
dvdButton.addEventListener( "click" , dvdScreensaver );
