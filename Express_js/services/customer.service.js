const boom = require("@hapi/boom");
const { models } = require("./../libs/sequelize");

class CustomerService {
  constructor() {}

  async create(data) {
    const newCustomer = await models.Customer.create(data);
    return newCustomer;
  }

  async find() {
    const rta = await models.Customer.findAll();
    return rta;
  }

  async findOne(id) {}

  async update(id, changes) {}

  async delete(id) {}
}

module.exports = CustomerService;
