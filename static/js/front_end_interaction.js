$('#startstop').click(function() {
    if($("#startstop").hasClass("btn-outline-success")) {
        $("#startstop").text("Stop");
        $("#startstop").addClass("btn-outline-danger");
        $("#startstop").removeClass("btn-outline-success");
    } else if($("#startstop").hasClass("btn-outline-danger")) {
        $("#startstop").text("Start");
        $("#startstop").addClass("btn-outline-success");
        $("#startstop").removeClass("btn-outline-danger");
    };
});
