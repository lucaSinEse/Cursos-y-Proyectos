import express from "express";
import cors from "cors";
import morgan from "morgan";

import estudiantesRoutes from "./routes/estudiantesRoutes";
import cursosRoutes from "./routes/cursosRoutes";
import profesoresRoutes from "./routes/profesoresRoutes";
const app = express();

app.use(morgan("dev"));
app.use(cors());

app.use("/estudiantes", estudiantesRoutes);
app.use("/profesores", profesoresRoutes);
app.use("/cursos", cursosRoutes);


app.get("/", (req, res) => {
  res.send("Hola Mundo");
});

app.listen(3000, () => {
  console.log("server activo");
});
