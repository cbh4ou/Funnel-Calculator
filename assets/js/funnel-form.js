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
    $("#prodselect").change(function () {
        if ($(this).val() > 1) {
            var i;
            var prodnum = 2

            

            for (i = $(this).val(); i > 1; i--) {
                var div = String.format('<div class="row"><div class="col-xl-6"><div class="form-group"><label for="prods">FE Product Option {0}</label><input type="url" class="form-control" id="url" placeholder=""></div></div><div class="col-xl-4"><div class="form-group"><label for="prods">Estimated Take Rate %</label><input type="url" class="form-control" id="url" placeholder=""></div></div></div>', prodnum);
                $(".feprods").append(div)
                prodnum++;
            }



        }
    });
    String.format = function () {
        // The string containing the format items (e.g. "{0}")
        // will and always has to be the first argument.
        var theString = arguments[0];

        // start with the second argument (i = 1)
        for (var i = 1; i < arguments.length; i++) {
            // "gm" = RegEx options for Global search (more than one instance)
            // and for Multiline search
            var regEx = new RegExp("\\{" + (i - 1) + "\\}", "gm");
            theString = theString.replace(regEx, arguments[i]);
        }

        return theString;
    }

})(jQuery);