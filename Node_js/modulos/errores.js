function otraFuncion() {
  seRompe();
}

function seRompe() {
  return 3 + z;
}

function seRompeAsincrona(cb) {
  setTimeout(function () {
    try {
      return 3 + z;
    } catch (error) {
      console.error("Error en la funcion asincrona");
      cb(err);
    }
    return 3 + z;
  });
}

try {
  // otraFuncion();
  seRompeAsincrona(function (err) {
    console.log("Hay error: ", err);
  });
} catch (err) {
  console.error("Algo se rompio: ", err.message);
  console.log("Pero no pasa na");
}

console.log("Esto es un log fuera del try catch");
