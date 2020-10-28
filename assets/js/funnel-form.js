(function ($) {
    "use strict";
    $(".next1").click(function () {
        $(".step1").addClass('d-none')
        $(".step2").removeClass('d-none');

    });
    // Binding next button on second step
    $(".next2").click(function () {
        $(".step2").addClass('d-none')
        $(".step3").removeClass('d-none');

    });
    // Binding back button on second step
    $(".next3").click(function () {
        $(".step3").addClass('d-none')
        $(".step4").removeClass('d-none');

    });
    // Binding back button on third step
    $(".back2").click(function () {
        $(".step2").addClass('d-none')
        $(".step1").removeClass('d-none');

    });
    $(".back3").click(function () {
        $(".step3").addClass('d-none')
        $(".step2").removeClass('d-none');

    });
    $(".back4").click(function () {
        $(".step4").addClass('d-none')
        $(".step3").removeClass('d-none');

    });
    $(".open3").click(function () {

        // optional
        // used delay form submission for a seccond and show a loader image
        $("#loader").show();
        setTimeout(function () {
            $("#basicform").html('<h2>Thanks for your time.</h2>');
        }, 1000);
        // Remove this if you are not using ajax method for submitting values
        return false;

    });
})(jQuery);