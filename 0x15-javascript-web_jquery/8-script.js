#!/usr/bin/node

$.ajax({
  method: "GET",
  url: "https://swapi-api.alx-tools.com/api/films/?format=json",
  success: function (data) {
    $('UL#list_movies').append(data.results.map(movie => `<li>${movie.title}</li>`));
  }
});