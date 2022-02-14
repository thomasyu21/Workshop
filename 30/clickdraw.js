// Raymond Yeung, Thomas Yu
// SoftDev pd1
// K
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
    	return "Circle"
    }else{
    	mode = "rect";
    	console.log(mode);
    	return "Rectangle";
    }
}

let drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log(mouseX);
    console.log(mouseY);
}

let drawCircle = function(e) {
    console.log("test");
}

let draw = function(e){

}

let wipeCanvas = function(){
    ctx.clearRect(0,0, canvas.width, canvas.height);
}

c.addEventListener("clicK", drawRect);

let buttonToggle = document.getElementById("buttonToggle");
buttonToggle.addEventListener("click", event => {
    buttonToggle.innerText = toggleMode(c);
});
