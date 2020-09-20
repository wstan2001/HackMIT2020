time_list = [];

$(document).ready(function() {
    $("#post_button").click(function() {
        var date = new Date();
        var timestamp = date.getDate() + "/" + (date.getMonth() + 1) + " " 
                        + date.getHours() + ":" + date.getMinutes();

        console.log("clicked! At " + timestamp);

        //needs to send over relevant data to the database

        //also needs to update marker popups

        var time = document.getElementById("wait_time").value;
        console.log(time);

        var location = document.getElementById("curr_loc").innerHTML;
        console.log("Location: " + location);


        //need to update label of marker with new wait time
        var idx = -1;
        for (var i = 0; i < markers.length; i++) {
            var marker_loc = markers[i]._popup.getContent();    //temp variable
            marker_loc = marker_loc.replace(/<[^>]*>/g, '');
            if (marker_loc.length < location.length) {
                continue;
            }
            else if (location === marker_loc.slice(0, location.length)) {
                idx = i;
                break;
            }
        }
        if (idx === -1) {
            console.log("Something very bad happened; location posted to not found");
        }
        else {
            markers[i]._popup.setContent('<p>' + location + '</p>' + 
            '<p> Estimated wait time: ' + time + ' </p>' + 
            '<p> Last Updated: ' + timestamp + ' </p?');
        }
    });
});

