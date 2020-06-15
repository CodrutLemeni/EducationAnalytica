/** HBC stands for Horizontal Bar Charts */
const express = require("express");
const Validator = require("validatorjs");

exports.getRouter = ({ config, db }) => {
  const hbc = express.Router();

  /** Filtering all requests that are not looking for a horizontal bar chart */
  hbc.all("*", (req, res, next) => {
    if (req.query.type !== undefined || req.query.type !== "hbc") next();
  });

  hbc.get("/:subfolder/:year", (req, res) => {
    /**
     * Validating correct URL parameters
     */
    const validationRules = {
      year: ["integer"],
      subfolder: ["string", "alpha_dash"],
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

    /**
     * Validating that we have the requested data
     */
    const dataRules = {
      year: ["in:2015,2016,2017,2019"],
      subfolder: [
        `in:${config.hbc_subfolders.reduce((acc, val) => {
          if (acc === "") acc = val;
          else acc += "," + val;
          return acc;
        })}`,
      ],
    };
    const dataValidation = new Validator(params, dataRules);

    if (dataValidation.fails()) {
      return res.status(404).json({
        error: {
          code: 404,
          msg: "Content not found",
          description: `Your request was correct, but we do not have that data yet. If you would like to see it added, send us an email at ${config.contactEmail}`,
        },
      });
    }

    const { data, err } = db.getHBC(params);

    if (err) {
      // TODO: Add some error logging.
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

  return hbc;
};
