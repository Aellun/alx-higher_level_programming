// fetches and lists the title for all movies
$(document).ready(function () {
    $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function (data) {
        $.each(data.results, function (_, film) {
            $("<li>", { text: film.title }).appendTo("ul#list_movies");
        });
    });
});
