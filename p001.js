Array.prototype.max = function() {
 return Math.max.apply(null, this)
}

Array.prototype.min = function() {
 return Math.min.apply(null, this)
}

function timesPerSecond(f){
 var n = 1;
 while(true){
   var t = new Date();
   for(var i=0; i<n; ++i){
     f();
   }
   var dt = (new Date()) - t;
   if (dt<100){
     n *= 10;
   }else{
     return Math.floor(n / dt * 1000);
   }
 }
}

function getPerformance(N, f){
 var a = Array();
 for (var i=0; i<N; i++){
   a.push(timesPerSecond(f));
 }
 console.log("min : " + a.min() + " times / sec");
 console.log("max : " + a.max() + " times / sec");
}

function solve_a(N){
 // add approaching
 var a = 0;
 for (var i=1; i<N; i++){
   a += (!(i%3)||!(i%5)) ? i : 0;
 }
 return a;
}

function solve_b(N){
 // minus approaching
 var a = N*(N-1)/2;
 for (var i=1; i<N; i++){
   a -= ((i%3)&&(i%5)) ? i : 0;
 }
 return a;
}

N = 1000;
T = 30;
console.log("plus approach - ans : " + solve_a(N));
getPerformance(T, solve_a.bind(null, N));
console.log("minus approach - ans : " + solve_b(N));
getPerformance(T, solve_b.bind(null, N));
