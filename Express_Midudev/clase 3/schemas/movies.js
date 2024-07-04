const z = require("zod");

movieSchema = z.object({
  title: z.string({
    invalid_type_error: "movie title must be a string",
    required_error: "title is required",
  }),
  year: z.number().int().min(1900).max(2025),
  director: z.string(),
  duration: z.number().int().positive(),
  rate: z.number().min(0).max(10),
  poster: z.string().url({
    message: "Poster must be a valid URL",
  }),
  genre: z.array(
    z.enum([
      "Fantasy",
      "Biography",
      "Animation",
      "Romance",
      "Sci-Fi",
      "Adventure",
      "Action",
      "Crime",
      "Drama",
    ])
  ),
});

function validateMovie(object) {
  return movieSchema.safeParse(object);
}

function validatePartialMovie (object) {
  return movieSchema.partial().safeParse(object);
}

module.exports = { validateMovie, validatePartialMovie };
