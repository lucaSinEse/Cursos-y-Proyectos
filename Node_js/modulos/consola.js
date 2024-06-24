console.log("Algo");
console.error("error");
console.warn("Warning");

var tabla = [
  {
    a: 1,
    b: "z",
  },
  {
    a: 2,
    b: "m",
  },
];
console.table(tabla);

console.group("Conver");
console.log("Hola");
console.log("Bla bla bla");
console.log("Adios");
console.groupEnd("Conver");