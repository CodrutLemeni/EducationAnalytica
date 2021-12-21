const express = require("express");
const Validator = require("validatorjs");
const distribuitons = require("./distributions");
const hbc = require("./hbc");
const mapcharts = require("./mapcharts");
const linegraphs = require("./linegraphs");
const package = require("../package.json");

exports.getRouter = ({ config, db }) => {
  const api = express.Router();

  api.use(
    `/${config.grade_distrib_root}`,
    distribuitons.getRouter({ config, db })
  );

  api.use(`/${config.hbc_root}`, hbc.getRouter({ config, db }));

  api.use(`/${config.map_chart_root}`, mapcharts.getRouter({ config, db }));

  api.use(`/${config.lc_root}`, linegraphs.getRouter({ config, db }));

  api.get("/", (req, res) => {
    const { name, version, description } = package;
    res.json({
      name,
      version,
      description,
    });
  });

  /** 404 Route, allways keep last */
  api.use("*", (req, res, next) => {
    res.status(404).json({
      error: {
        code: 404,
        msg: "Content not found",
        description:
          "We don't know what you are looking for, but make sure the URL is correct",
      },
    });
  });

  return api;
};
