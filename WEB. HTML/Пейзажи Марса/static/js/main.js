$(document).ready(function() {
    $('.carousel').carousel({
        interval: 2000
    })

    $(".carousel-control-next").click(() => $(".carousel").carousel("next"));
    $(".carousel-control-prev").click(() => $(".carousel").carousel("prev"));
});