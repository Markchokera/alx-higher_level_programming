const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    showHello();
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      showHello();
    }
  });
};
