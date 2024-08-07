$("document").ready(function () {
  $("#btn_translate").on("click", function () {
    $.get("https://www.fourtonfish.com/hellosalut/hello/" + $.param({lang: $("#language_code").val() }), function (data) {
      $("#hello").html(data.hello);
    });
  });
});

