$(document).ready(function () {
    var socket = io.connect();

    // Indicate Connection
    socket.on("connect", function (msg) {
        console.log("connected")
    });

    socket.on("update_data",function (msg) {
        console.log("Counter: " + msg.value);
        $("#value").text(msg.value);
    });
});
