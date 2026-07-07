fetch("gallery.json")

.then(response => response.json())

.then(images => {


const gallery =
document.getElementById("gallery");



images.forEach(photo=>{


let div =
document.createElement("div");


div.className="card";



div.innerHTML = `

<img src="images/thumbs/${photo.thumb}"
alt="${photo.title}">

<p>${photo.title}</p>

`;



div.onclick=function(){

openLightbox(
"images/full/"+photo.file
);

};



gallery.appendChild(div);



});


});
