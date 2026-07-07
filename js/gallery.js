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



div.onclick = function(){

    const img =
    "images/full/" + photo.file;

    openLightbox(img);

};



gallery.appendChild(div);



});


});
