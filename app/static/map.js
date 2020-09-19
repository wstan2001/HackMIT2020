var map = L.map( 'map', {
    center: [36.1, -79.4],
    maxZoom: 18,
    minZoom: 4,
    zoom: 11
});

L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: ['a','b','c']
}).addTo( map );


//wow for some reason I don't need to load markers from the JSON file?
for (var i = 0; i < markers.length; i++) {
  L.marker( [markers[i].lat, markers[i].lng] )
      .bindPopup( '<p>' + markers[i].name + '</p>' + 
            '<p> Estimated wait time: ?? </p>' )
      .addTo( map );
}