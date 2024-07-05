import express, { json } from "express"; // require -> commonJS
import { movieRouter } from "./routes/movies.router.js";
import { corsMiddleware } from "./middlewares/cors.js";

const app = express();
app.use(json());
app.disable("x-powered-by"); // deshabilitar el header X-Powered-By: Express
app.use(corsMiddleware());

app.use("/movies", movieRouter);

const PORT = process.env.PORT ?? 1234;

app.listen(PORT, () => {
  console.log(`server listening on port http://localhost:${PORT}`);
});
