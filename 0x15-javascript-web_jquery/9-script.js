#!/usr/bin/node
$(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
});
