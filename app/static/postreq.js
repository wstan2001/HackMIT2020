time_list = [];

$(document).ready(function() {
    $("#post_button").click(function() {
        console.log("moo!");
        var time = document.getElementById("wait_time").value;
        console.log(time);
        document.getElementById("test").innerHTML = "You clicked it!";
    });
});

