const http = require("node:http");

const processRequest = (req, res) => {
  const { method, url } = req;

  switch (method) {
    case "GET":
      switch (url) {
        case "/":
          res.setHeader("Content-Type", "text/html; charset=utf-8");
          return res.end("<h1> Mi Página</h1>");
        case "/about":
          res.setHeader("Content-Type", "text/html; charset=utf-8");
          return res.end("<h1>About</h1>");
        default:
          res.statusCode = 404;
          res.setHeader("Content-Type", "text/html; charset=utf-8");
          return res.end("<h1>404</h1>");
      }
    case "POST":
      switch (url) {
        case "/":
          let body = "";
      }
    default:
      res.statusCode = 404;
      res.setHeader("Content-Type", "text/html; charset=utf-8");
      return res.end("<h1>404</h1>");
  }
};

const server = http.createServer(processRequest);

server.listen(1234, () => {
  console.log("server listening on port http://localhost:1234");
});
