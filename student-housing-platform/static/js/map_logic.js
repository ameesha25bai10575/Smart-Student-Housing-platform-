function initMap(){
    var map = L.map('map').setView([23.25,77.41],10);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    var listings = JSON.parse(document.getElementById("data").textContent);

    listings.forEach(l=>{
        L.marker([l.lat,l.lng]).addTo(map).bindPopup(l.title);
    });
}