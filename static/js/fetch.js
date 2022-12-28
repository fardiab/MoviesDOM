function Rest() {
    const url = '/popular_movies';
    fetch(url)
        .then((response) => response.json())
        .then(data => p_movies = data)
        .then(todo => p_movies.forEach(movie => {
            // Nbutton = '<button class="btn btn-primary" onclick="get_movie(' + movie.id + ')">More Info</button>';
            movie.innerHTML += '<div class="slide_inner_card"><div class="slider_poster"><img src="' + movie.image + '" alt="" width="265" height="392"><h4>' + movie.title + '</h4></div>'
        }));
}