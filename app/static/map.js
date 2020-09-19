var map = L.map( 'map', {
    center: [35.75, -79],
    maxZoom: 17,
    minZoom: 4,
    zoom: 7
});

L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: ['a','b','c']
}).addTo( map );


//wow for some reason I don't need to load markers from the JSON file?
for (var i = 0; i < markers.length; i++) {
  L.marker( [markers[i].lat, markers[i].lng] )
      .bindPopup( '<p">' + markers[i].name + '</p>' )
      .addTo( map );
}