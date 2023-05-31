$(document).ready(function () {
	$.getJSON(
		"https://swapi-api.alx-tools.com/api/films/?format=json",
		function (data) {
			data.results.forEach(function (film) {
				$("<li>").text(film.title).appendTo("ul#list_movies");
			});
		}
	);
});

/*
 JavaScript script that fetches and lists the title for
 all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
*/
