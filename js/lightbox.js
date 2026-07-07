const lightbox =
document.getElementById("lightbox");


const image =
document.getElementById("lightbox-img");



function openLightbox(src){

image.src=src;

lightbox.style.display="flex";

}



lightbox.onclick=function(){

lightbox.style.display="none";

}
