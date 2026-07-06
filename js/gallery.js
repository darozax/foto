fetch("gallery.json")

.then(response=>response.json())

.then(data=>{

const gallery=document.getElementById("gallery");

data.forEach(photo=>{

const div=document.createElement("div");

div.className="photo";

div.innerHTML=`

<img
loading="lazy"
src="images/thumbs/${photo.file}"
data-full="images/full/${photo.file}"
alt="${photo.title}"
>

<p>${photo.title}</p>

`;

gallery.appendChild(div);

});

});
