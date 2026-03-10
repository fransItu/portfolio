// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {

anchor.addEventListener("click", function (e) {

e.preventDefault();

document.querySelector(this.getAttribute("href")).scrollIntoView({
behavior: "smooth"
});

});

});


// Typing effect for hero title
const text = "Software Developer | Python | Linux";
let index = 0;

function typeEffect() {

if(index < text.length){

document.getElementById("typing").innerHTML += text.charAt(index);

index++;

setTimeout(typeEffect, 50);

}

}

window.onload = typeEffect;


// Simple fade-in animation on scroll
const sections = document.querySelectorAll(".section");

window.addEventListener("scroll", () => {

sections.forEach(section => {

const position = section.getBoundingClientRect().top;
const screenPosition = window.innerHeight / 1.3;

if(position < screenPosition){
section.style.opacity = 1;
section.style.transform = "translateY(0)";
}

});

});
