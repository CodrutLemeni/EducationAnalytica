const express = require("express");
const Validator = require("validatorjs");
const distribuitons = require("./distributions");
const hbc = require("./hbc");
const package = require("../package.json");

exports.getRouter = ({ config, db }) => {
  const api = express.Router();

  api.use("/grade-distributions", distribuitons.getRouter({ config, db }));
  api.use(`/${config.hbc_root}`, hbc.getRouter({ config, db }));

  api.get("/", (req, res) => {
    const { name, version, description } = package;
    res.json({
      name,
      version,
      description,
    });
  });

  return api;
};
