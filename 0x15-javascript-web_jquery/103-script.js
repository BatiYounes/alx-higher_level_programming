$('document').ready(function () {
  $('#btn_translate').on("click", translateIt);
  $('#language_code').on("focus", function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translateIt();
      }
    });
  });
});

function translateIt () {
  const api = 'https://www.fourtonfish.com/hellosalut/hello/';
  $.get(api + $.param({lang: $('#language_code').val()}), function (data) {
    $('#hello').html(data.hello);
  });
}

