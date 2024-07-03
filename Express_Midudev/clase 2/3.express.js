const express = require("express");

const PORT = process.env.PORT ?? 1234;

const app = express();
//! Buena practica sacar esto
app.disable("x-powered-by");

app.use((req, res, next) => {
  if (req.method !== "POST") return next();
  if (req.headers["content-type"] !== "application/json") return next();

  // solo llegan request POST y que tienen header COntent-Type application/json
  let body = "";

  req.on("data", (chunk) => {
    body += chunk.toString();
  });

  req.on("end", () => {
    const data = JSON.parse(body);
    data.timestamp = Date.now();
    req.body = data;

    next();
  });
});

app.get("/", (req, res) => {
  res.send("<h1> Mi Página</h1>");
});

app.post("/posteo", (req, res) => {
  res.status(201).json(req.body);
});

// La ultima a la que va a llegar
app.use((req, res) => {
  res.status(404).send("<h1>404</h1>");
});

app.listen(PORT, () => {
  console.log(`server listening on port http://localhost:${PORT}`);
});
