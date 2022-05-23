// const selectElement = (element) => document.querySelector(element);
// var path = window.location.pathname;
// var page = path.split("/").pop();
// window.onscroll = function() {scrollFunction()};
var input = document.getElementsByClassName("telephone");
console.log(input);
for(var i=0;i<input.length;i++)
{
window.intlTelInput(input[i],({
allowDropdown:true,
initialCountry:"np",
}));
}
var login = document.getElementById("login-pressed").innerHTML;
var register= document.getElementById("register-pressed").innerHTML;
document.getElementById("login-pressed").innerHTML="";
function login_click(){
  console.log(login);
  document.getElementById("register-pressed").innerHTML="";
  document.getElementById("register-pressed").innerHTML=login;
  document.getElementById("register-heading").innerHTML="Login To Continue";
}
function register_click(){
  console.log(register);
  document.getElementById("register-pressed").innerHTML="";
  document.getElementById("register-pressed").innerHTML=register;
  document.getElementById("register-heading").innerHTML="Register To Access Our Service";
}
// if(page!="index.html"){
  
//   document.getElementById("navbar").style.padding = "20px 10px";
//   document.getElementById("logo").style.height = "5rem";
//   document.getElementById("logo").style.width = "5rem";
//   document.getElementById("navbar").style.backgroundColor="white";
//   var elements=document.getElementsByClassName("nav-item-color");
//   for(var i=0;i<elements.length;i++)
//     {
//       elements[i].style.color="#D35F8D";
//     }
// }

// selectElement('.menu-icons').addEventListener('click',()=>{
// 	selectElement('nav').classList.toggle('active');
// });

// function login_clicked(){

// }

// function scrollFunction() {
//   if ((document.body.scrollTop > 50 || document.documentElement.scrollTop > 50)&&window.innerWidth>900) {
//     document.getElementById("navbar").style.padding = "20px 10px";
//     document.getElementById("logo").style.height = "5rem";
//     document.getElementById("logo").style.width = "5rem";
//     document.getElementById("navbar").style.backgroundColor="white";
//     var elements=document.getElementsByClassName("nav-item-color");
//     for(var i=0;i<elements.length;i++)
//     {
//     	elements[i].style.color="#D35F8D";
//     }

//   }
//   else if(window.innerWidth<900)
//   {
//   	document.getElementById("navbar").style.padding = "5px";
//     document.getElementById("logo").style.height = "5rem";
//     document.getElementById("logo").style.width = "5rem";
//   } else {
//     document.getElementById("navbar").style.padding = "80px 15px";
//     document.getElementById("logo").style.height = "7rem";
//     document.getElementById("logo").style.width = "7rem";
//     document.getElementById("navbar").style.backgroundColor="transparent";
//     var elements=document.getElementsByClassName("nav-item-color");
//     for(var i=0;i<elements.length;i++)
//     {
//     	elements[i].style.color="#000";
//     }

//   }
// }

