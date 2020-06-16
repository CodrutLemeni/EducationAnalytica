const express = require("express");
const Validator = require("validatorjs");

exports.getRouter = ({ db, config }) => {
  const mapcharts = express.Router();

  mapcharts.get("/:year", (req, res) => {
    /**
     * Validating correct URL parameters
     */
    const validationRules = {
      year: ["integer", "in:2015,2016,2017,2019"],
    };
    const params = { ...req.params };
    const validation = new Validator(params, validationRules);

    if (validation.fails()) {
      return res.status(400).json({
        error: {
          code: 400,
          msg: "URL parameters are not formated corectly.",
          errors: validation.errors.all(),
        },
      });
    }

    const { data, error } = db.getMapChart({ year: req.params.year });

    if (error) {
      console.error(`ERROR: ${error}`);
      return res.status(500).json({
        error: {
          code: 500,
          msg: "Internal server error",
          description: "There was an error retreiving the data",
        },
      });
    }

    res.status(200).json(data);
  });

  return mapcharts;
};
