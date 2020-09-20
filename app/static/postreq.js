$(document).ready(function() {
    $("#post_button").click(function() {
        var date = new Date();
        var timestamp = date.getDate() + "/" + (date.getMonth() + 1) + " " 
                        + date.getHours() + ":" + date.getMinutes();

        console.log("clicked! At " + timestamp);

        //needs to send over relevant data to the database

        //also needs to update marker popups

        var waittime = document.getElementById("wait_time").value;
        console.log(waittime);

        const url = "/donkey";
        $.ajax({
            url : url
        });

    });
});

