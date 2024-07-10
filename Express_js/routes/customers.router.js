const express = require("express");
const CustomerService = require("./../services/customer.service");
const validatorHandler = require("./../middlewares/validator.handler");
const {
  getCustomerSchema,
  createCustomerSchema,
  updateCustomerSchema,
} = require("./../schemas/customer.schema");

const router = express.Router();
const service = new CustomerService();

router.get("/", async (req, res, next) => {
});

router.get("/:id", async (req, res, next) => {});

router.post("/", async (req, res, next) => {});

router.patch("/:id", async (req, res, next) => {});

router.delete("/:id", async (req, res, next) => {});

module.exports = router;
