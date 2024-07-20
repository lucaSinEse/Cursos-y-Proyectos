"use strict";
const {
  CategorySchema,
  CATEGORY_TABLE,
} = require("./../models/category.model");

const { ProductSchema, PRODUCT_TABLE } = require("./../models/product.model");

module.exports = {
  async up(queryInterface) {
    await queryInterface.createTable(CATEGORY_TABLE, CategorySchema.role);
    await queryInterface.createTable(PRODUCT_TABLE, ProductSchema.role);
  },

  async down(queryInterface) {
    await queryInterface.dropTable(CATEGORY_TABLE);
    await queryInterface.dropTable(PRODUCT_TABLE);
  },
};
