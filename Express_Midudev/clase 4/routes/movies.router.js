import { Router } from "express";
import { validateMovie, validatePartialMovie } from "../schemas/movies.js";
import { MovieModel } from "../models/movie.models.js";

export const movieRouter = Router();

movieRouter.get("/", async(req, res) => {
  try {
    const { genre } = req.query;
    const movies = await MovieModel.getAll({genre});
    res.json(movies);
  } catch (error) {
    
  }
});

movieRouter.get("/:id", async (req, res) => {
  const { id } = req.params;
  const movie = await MovieModel.getById({id});
  if (movie) return res.json(movie);

  res.status(404).json({ message: "Movie not found" });
});

movieRouter.post("/", async (req, res) => {
  const result = validateMovie(req.body);

  if (!result.success) {
    // 422 Unprocessable Entity
    return res.status(400).json({ error: JSON.parse(result.error.message) });
  }
  const newMovie = await MovieModel.create(result.data)
  res.status(201).json(newMovie);
});

movieRouter.delete("/:id", async(req, res) => {
  const { id } = req.params;
  const movieIndex = await MovieModel.delete({id});
  if(!movieIndex){
    return res.status(404).json({ message: "Movie not found" });
  }
  return res.json({ message: "Movie deleted" });
});

movieRouter.patch("/:id", async (req, res) => {
  const result = validatePartialMovie(req.body);

  if (!result.success) {
    return res.status(400).json({ error: JSON.parse(result.error.message) });
  }

  const { id } = req.params;
  const updatedMovie = await MovieModel.update({id, input: result.data})

  if (updatedMovie === false) {
    return res.status(404).json({ message: "Movie not found" });
  }
  return res.json(updatedMovie);
});
