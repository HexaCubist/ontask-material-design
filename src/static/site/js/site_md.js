// Button Ripples
// mdc.ripple.MDCRipple.attachTo($('.mdc-ripple-js'));
// Top App bar Instantiation
// const topAppBarElement = document.querySelector('.mdc-top-app-bar');
// const topAppBar = new MDCTopAppBar(topAppBarElement);

// Auto Init
window.mdc.autoInit();

// Navigation Effect
$(function() {
    $(window).bind("load resize", function() {
        topOffset = 101;
        width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
        if (width < 839) {
            $('.siderail').removeClass('siderail-open');
            topOffset = 100; // 2-row-menu
        } else {
            $('.siderail').addClass('siderail-open');
        }
    });

    var url = window.location;
    var element = $('a.mdc-list-item').filter(function() {
        if (this.href == url) return true;
        return this.classList.contains("action-sub") && url.href.indexOf("/action/") > -1;
    }).addClass('mdc-list-item--activated');
});


var set_qbuilder = function (element_id, qbuilder_options, builder_element="#builder") {
    var id_formula_value = $(element_id).val();
    if (id_formula_value != "null" && id_formula_value != "{}") {
      qbuilder_options["rules"] = JSON.parse(id_formula_value);
    }
    $(builder_element).queryBuilder(qbuilder_options);
};
var set_element_select = function(element_id) {
  $(element_id).searchableOptionList({
    maxHeight: "250px",
    showSelectAll: true,
    texts: {
      searchplaceholder: gettext("Click here to search"),
      noItemsAvailable: gettext("No element found")
    }
  });
 };
var insert_fields = function (the_form) {
    if (document.getElementById("id_filter") != null) {
      formula = $("#builder").queryBuilder("getRules");
      if (formula == null || !formula["valid"]) {
        return false;
      }
      f_text = JSON.stringify(formula, undefined, 2);
      $("#id_filter").val(f_text);
    }
    return true;
};
var get_id_content = function() {
  if (typeof $("#id_content").summernote != "undefined") {
    value = $("#id_content").summernote("code");
  } else {
    value = $("#id_content").val();
  }
  return value;
};
var loadForm = function () {
    console.log("Opening form for element:");
    console.log(this);
    $(".mdc-dialog .dialog__surface").html("");
    var btn = $(this);
    if ($(this).is("[class*='disabled']")) {
      return;
    }
    data = {};
    if (document.getElementById("id_subject") != null) {
      data["subject_content"] = $("#id_subject").val();
    }
    $.ajax({
      url: btn.attr("data-url"),
      type: "get",
      dataType: "json",
      data: data,
      beforeSend: function() {
        $(".mdc-dialog .dialog__surface").html("");
        dialog.open();
      },
      success: function(data) {
        console.log(data)
        if (data.form_is_valid) {
          if (data.html_redirect == "") {
            $("#div-spinner").show();
            window.location.reload(true);
          } else {
            location.href = data.html_redirect;
          }
          return;
        }
        $(".mdc-dialog .mdc-dialog__surface").html(data.html_form);
        window.mdc.autoInit();
        if (document.getElementById("id_formula") != null) {
          set_qbuilder('#id_formula', qbuilder_options);
        }
        if (document.getElementById("id_columns") != null) {
          set_element_select("#id_columns");
        }
      },
      error: function(jqXHR, textStatus, errorThrown) {
        $("#div-spinner").show();
        location.reload(true);
      }
    });
};
var saveForm = function () {
    console.log("Saving form for element:");
    console.log(this);
    var form = $(this);
    if (this.querySelector("#id_formula") != null) {
      formula = $(this.querySelector("#builder")).queryBuilder('getRules');
      if (formula == null || !formula['valid']) {
        return false;
      }
      f_text = JSON.stringify(formula, undefined, 2);
      $(this.querySelector("#id_formula")).val(f_text);
    }
    var data = form.serializeArray();
    if (this.querySelector("#id_content") != null) {
      value = get_id_content(elem=this.querySelector("#id_content"));
      data.push({"name": "action_content", "value": value});
    }
    // $(this).parent().html("");
    $.ajax({
      url: form.attr("action"),
      data: data,
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          if (data.html_redirect == "") {
            $('#div-spinner').show();
            window.location.reload(true);
          } else {
            location.href = data.html_redirect;
          }
        }
        else {
          // $("#modal-item .modal-content").html(data.html_form);
          if (this.querySelector("#id_formula") != null) {
            set_qbuilder('#id_formula', qbuilder_options);
          }
          if (this.querySelector("#id_columns") != null) {
            set_element_select("#id_columns");
          }
        }
      },
      error: function(jqXHR, textStatus, errorThrown) {
        $('#div-spinner').show();
        location.reload(true);
      }
    });
    return false;
};
// $(document).ready(function(){
//   $('[data-toggle="tooltip"]').tooltip({
//     trigger: "hover",
//     placement: "auto",
//     container: "body"
//   });
//   $("body").on("click", ".spin", function () {
//     $('#div-spinner').show();
//   });
// });
// $(window).bind("load", function() {
//    $('#div-spinner').hide();
// });
// $(':input').on('invalid', function(e){
//   $('#div-spinner').hide();
// });