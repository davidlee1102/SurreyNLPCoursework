$(document).ready(function () {
    $(".layer").on("mouseenter", function () {
        $(this).find(".layer-details").fadeIn(200);
    });

    $(".layer").on("mouseleave", function () {
        $(this).find(".layer-details").fadeOut(200);
    });
});
