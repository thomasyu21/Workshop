// Raymond Yeung, Thomas Yu
// SoftDev pd1
// K30
// 2022-02-14

//retrieve node in DOM via ID
let c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
let ctx = c.getContext("2d");

//init global state var
let mode = "rect";

let toggleMode = function(e) {
    console.log("toggling...");
    if (mode === "rect"){
    	mode = "circ";
    	console.log(mode);
    	e.target.innerHTML = "Circle"
    }else{
    	mode = "rect";
    	console.log(mode);
    	e.target.innerHTML = "Rectangle"
    }
}

let drawRect = function(e) {
  let mouseX = e.offsetX;
  let mouseY = e.offsetY;
  console.log("mouseclick registered at ", mouseX, mouseY);
  ctx.beginPath();
  ctx.rect(mouseX, mouseY, 100, 200);
  ctx.fillStyle = "red";
  ctx.fill();
}

let drawCircle = function(e) {
    let mouseX = e.offsetX;
    let mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle = "red";
    ctx.strokeStyle = "black";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
}

let draw = function(e){
  if (mode === "rect"){
    drawRect(e);
  }else{
    drawCircle(e);
  }
}

let wipeCanvas = function(){
    console.log("wiping");
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw);

let buttonToggle = document.getElementById("buttonToggle");
buttonToggle.addEventListener("click", toggleMode);

let clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);
