const http = require("http");

http.createServer(router).listen(3000);

function router(req, res) {
  //request y response
  console.log("nueva peticion");
  console.log(req.url);

  switch (req.url) {
    case "/hola":
      res.write("Hola, que tal?");
      res.end();
      break;
    default:
      res.write("Error 404 ni idea");
      res.end();
  }
  // res.writeHead(201, { "COntent-Type": "text/plain" });
  // res.write("Hola, god http eh");
  // res.end();
}
console.log("estas escuchando http en el puerto 3000");
