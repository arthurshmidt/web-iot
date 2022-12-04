$(document).ready(function () {
    var socket = io.connect();
    var data = {
        "startstop": 0
    }
    // Indicate Connection
    socket.on("connect", function (msg) {
        console.log("connected");
    });

    socket.on("update_data",function (msg) {
        console.log("Counter: " + msg.value);
        $("#value").text(msg.value);
    });

    socket.on("update_stpt",function (msg) {
        console.log("startstop stpt: " + msg.startstop);
        $("#startstopvalue").text(msg.startstop);
    });

    // Update Set Points and Emit them
    var intervalId = window.setInterval(function () {
        // Update Set Points
        if($("#startstop").val() == "started") {
            data["startstop"] = 1;
        } else if($("#startstop").val() == "stopped") {
            data["startstop"] = 0;
        };

        // Emit updated Setpoints
        socket.emit("stpt",data);
        console.log(data);
    }, 1000);
});
