const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  data.results.forEach((obj) => {
    $('UL#list_movies').append(`<LI>${obj.title}</LI>`);
  });
});
