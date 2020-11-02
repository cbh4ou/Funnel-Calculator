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
            var prodnum = 2;



            for (i = $(this).val(); i > 1; i--) {
                var div = String.format('<div class="row">\
                <div class="col-xl-6">\
                  <div class="form-group">\
                    <label for="prods">FE Product Option {0}</label>\
                    <input type="text" name="prod{0}" class="form-control" id="text" placeholder="">\
                  </div>\
                </div>\
                <div class="col-xl-2">\
                  <div class="form-group">\
                    <label for="prods">Product Price</label>\
                    <input type="number" min="0" name="prod_price{0}" class="form-control" id="text" placeholder="">\
                  </div>\
                </div>\
                <div class="col-xl-2">\
                  <div class="form-group">\
                    <label for="prods">Product/Freight Cost</label>\
                    <input type="number" min="0" name="prod_cost{0}" class="form-control" id="text" placeholder="">\
                  </div>\
                </div>\
                <div class="col-xl-2">\
                  <div class="form-group">\
                    <label for="prods">Est. Take Rate %</label>\
                    <input type="number" min="0" name="prod_tr{0}" class="form-control" id="text" placeholder="">\
                  </div>\
                </div>\
              </div>', prodnum);
                $(".feprods").append(div)
                prodnum++;
            }



        }
    });
    $("#bumpselect").change(function () {
        if ($(this).val() > 1) {
            var i;
            var prodnum = 2;



            for (i = $(this).val(); i > 1; i--) {
                var div = String.format('<div class="row">\
                <div class="col-xl-6">\
                  <div class="form-group">\
                    <label for="prods">Order Bump Option {0}: Name</label>\
                    <input type="text" name="order_bump{0}" class="form-control" id="text" placeholder="">\
                  </div>\
                </div>\
                <div class="col-xl-2">\
                  <div class="form-group">\
                    <label for="prods">Product Price</label>\
                    <input type="number" min="0" name="ob_price{0}" class="form-control" id="text" placeholder="">\
                  </div>\
                </div>\
                <div class="col-xl-2">\
                  <div class="form-group">\
                    <label for="prods">Product/Freight Cost</label>\
                    <input type="number" min="0" name="ob_cost{0}" class="form-control" id="text" placeholder="">\
                  </div>\
                </div>\
                <div class="col-xl-2">\
                  <div class="form-group">\
                    <label for="prods">Est. Take Rate %</label>\
                    <input type="number" min="0" name="ob_tr{0}" class="form-control" id="text" placeholder="">\
                  </div>\
                </div>\
              </div>', prodnum);
                $(".orderbumps").append(div)
                prodnum++;
            }



        }
    });
    $("#upselect").change(function () {
        if ($(this).val() > 1) {
            var i;
            var prodnum = 2;



            for (i = $(this).val(); i > 1; i--) {
                var div = String.format('<div class="row">\
                <div class="col-xl-6">\
                  <div class="form-group">\
                    <label for="prods">Upsell Option {0}: Name</label>\
                    <input type="text" name="up_name{0}" class="form-control" id="upsellselect" placeholder="">\
                  </div>\
                </div>\
                <div class="col-xl-2">\
                  <div class="form-group">\
                    <label for="prods">Product Price</label>\
                    <input type="number" min="0" name="up_price{0}" class="form-control" id="text" placeholder="">\
                  </div>\
                </div>\
                <div class="col-xl-2">\
                  <div class="form-group">\
                    <label for="prods">Product/Freight Cost</label>\
                    <input type="number" min="0" name="up_cost{0}" class="form-control" id="text" placeholder="">\
                  </div>\
                </div>\
                <div class="col-xl-2">\
                  <div class="form-group">\
                    <label for="prods">Est. Take Rate %</label>\
                    <input type="number" min="0" name="up_tr{0}" class="form-control" id="text" placeholder="">\
                  </div>\
                </div>\
              </div>', prodnum);
                $(".upsells").append(div)
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
    $("#product-cost-form").submit(function (e) {

        e.preventDefault(); // avoid to execute the actual submit of the form.

        var form = $(this);
        var url = '/funnel/create';

        $.ajax({
            type: "POST",
            url: url,
            data: form.serializeArray(), // serializes the form's elements.
            success: function (data) {
                alert(data); // show response from the php script.
                window.location = "/funnel/editor";
            }
        });
    });
})(jQuery);