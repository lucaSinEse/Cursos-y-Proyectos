// const process = require("process");

process.on('beforeExit', () =>{
  console.log('El proceso va a terminar');
});

process.on('exit', () =>{
  console.log('El proceso termino');
});

process.on("uncaughtException", (err, origen) =>{
  console.log('Se nos olvido capturar un error.');
  console.error(err);
})

// process.on("uncaugthRejection")

functionQueNoExiste();

console.log('esto si el error no se agarra');