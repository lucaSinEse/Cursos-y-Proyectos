function soyAsincrona(miCallback) {
  setTimeout(function () {
    console.log("Hola, soy una funcion asincrona");
    miCallback();
  }, 1000);
}
console.log("Iniciando proceso");
soyAsincrona(function () {
  console.log("Terminando proceso");
});
