const { UserSchema, User } = require("./user.model");
const { CustomerSchema, Customer } = require("./customer.model");

function setupModels(sequelize) {
  User.init(UserSchema, User.config(sequelize));
  Customer.init(CustomerSchema, Customer.config(sequelize));
}

module.exports = setupModels;