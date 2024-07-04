const express = require("express"); // require => commonJS
const crypto = require("node:crypto");
const moviesJSON = require("./movies.json");
const { validateMovie, validatePartialMovie } = require("./schemas/movies");
const z = require("zod");

const app = express();

app.use(express.json());
app.disable("x-powered-by");

app.get("/movies", (req, res) => {
  const { genre } = req.query;

  if (genre) {
    const filteredMovies = moviesJSON.filter((movie) =>
      movie.genre.some((g) => g.toLowerCase() === genre.toLowerCase())
    );
    return res.json(filteredMovies);
  }
  return res.json(moviesJSON);
});

app.get("/movies/:id", (req, res) => {
  //path-to-regexp
  const { id } = req.params;

  const movie = moviesJSON.find((movie) => movie.id === id);
  if (movie) return res.json(movie);

  return res.status(404).json({ message: "Movie not found" });
});

app.get("/movies?genre", (req, res) => {
  return res.json(moviesJSON);
});

app.post("/movies", (req, res) => {
  const result = validateMovie(req.body);

  if (result.error) {
    return res.status(400).json({ error: result.error.message });
  }
  const { title, genre, director, year, duration, rate, poster } = req.body;

  const newMovie = {
    id: crypto.randomUUID(),
    title,
    genre,
    director,
    year,
    duration,
    rate: rate ?? 0,
    poster,
  };
  moviesJSON.push(newMovie);

  return res.status(201).json(newMovie);
});

app.patch("/movies/:id", (req, res) => {
  const result = validatePartialMovie(req.body);

  if (!result.success) {
    return res.status(400).json(result.error.message);
  }

  const { id } = req.params;
  const movieIndex = moviesJSON.findIndex((movie) => movie.id === id);

  if (movieIndex === -1) {
    return res.status(404).json({ message: "movie not found" });
  }
  const updateMovie = {
    ...moviesJSON[movieIndex],
    ...result.data,
  };
  moviesJSON[movieIndex] = updateMovie;

  return res.json(updateMovie);
});

const PORT = process.env.PORT ?? 1234;

app.listen(PORT, () => {
  console.log(`server listening on port http://localhost:${PORT}`);
});
