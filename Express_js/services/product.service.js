const { faker } = require("@faker-js/faker");
const boom = require("@hapi/boom");

class ProductService {
  constructor() {
    this.products = [];
    this.generate();
  }

  generate() {
    const limit = 100;

    for (let i = 0; i < Number(limit); i++) {
      this.products.push({
        id: faker.string.uuid(),
        name: faker.commerce.productName(),
        price: Number(faker.commerce.price()),
        image: faker.image.url(),
        isBlock: faker.datatype.boolean(),
      });
    }
  }

  async create(product) {
    const uuid = faker.string.uuid();

    const newProduct = {
      uuid,
      name: product.name,
      price: product.price,
      image: product.image,
    };

    this.products.push(newProduct);

    return newProduct;
  }

  async find() {
    return this.products;
  }

  async findOne(id) {
    const product = this.products.find((item) => item.id === id);
    if (!product) {
      throw boom.notFound("Product not found.");
    }

    if (product.isBlock) {
      throw boom.conflict("Product block.");
    }
    return product;
  }

  async update(id, body = {}) {
    const index = this.products.findIndex((item) => item.id === id);

    if (index === -1) {
      throw boom.notFound("Product not found.");
    }
    const product = this.products[index];

    this.products[index] = {
      ...product,
      ...body,
    };

    return this.products[index];
  }

  async delete(id) {
    const index = this.products.findIndex((item) => item.id === id);

    if (index === -1) {
      throw boom.notFound("Product not found.");
    }

    this.products.splice(index, 1);
    return { message: "Deleted" };
  }
}

module.exports = ProductService;
