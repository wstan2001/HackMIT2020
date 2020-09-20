var map = L.map( 'map', {
    center: [35.7, -79.4],
    maxZoom: 18,
    minZoom: 4,
    zoom: 7
});

L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: ['a','b','c']
}).addTo( map );


var markers = new Array();

//wow for some reason I don't need to load markers from the JSON file?
//let here is important, won't work if i is var
for (let i = 0; i < locs.length; i++) {
  var temp = L.marker( [locs[i].lat, locs[i].lng] )
      .bindPopup( '<p>' + locs[i].name + '</p>' + 
        '<p> Estimated wait time: ?? </p>' )
          .on('click', function() {
            console.log(locs[i].name);
            $("#curr_loc").html(locs[i].name);
  });
  markers.push(temp);
  map.addLayer(temp);
  
  /*L.marker( [locs[i].lat, locs[i].lng] )
      .bindPopup( '<p>' + locs[i].name + '</p>' + 
            '<p> Estimated wait time: ?? </p>' )
      .addTo( map ).on('click', function() {
        console.log(locs[i].name);
        $("#curr_loc").html(locs[i].name);
      });*/
}