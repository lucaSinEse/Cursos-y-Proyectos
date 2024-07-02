const express = require("express");
const productsRouters = require("./products.router");
const usersRouters = require("./users.routers");
const categoriesRouters = require("./categories.router");

function routerApi(app) {
  const router = express.Router()
  app.use('/api/v1', router);
  
  router.use("/products", productsRouters);
  router.use("/users", usersRouters);
  router.use("/categories", categoriesRouters);
}

module.exports = routerApi;