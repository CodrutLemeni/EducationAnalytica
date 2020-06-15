const express = require("express");
const Validator = require("validatorjs");

exports.getRouter = ({ config, db }) => {
  const distributions = express.Router();

  /** Filtering all requests that are not looking for a grade distribution */
  distributions.all("*", (req, res, next) => {
    if (req.query.type !== undefined || req.query.type !== "garde-d") next();
  });

  distributions.get(
    "/:year/:gender/:region/:county/:course/:subject",
    (req, res) => {
      /**
       * Validating correct URL parameters
       */
      const validationRules = {
        year: ["integer", "in:2015,2016,2017,2019"],
        gender: ["string", "in:m,f,all"],
        region: ["string", "in:urban,rural,all"],
        county: "string",
        course: "string",
        subject: "string",
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
        gender: ["in:all"],
        region: ["in:all"],
        county: ["in:all"],
        course: ["in:all"],
        subject: ["in:all"],
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

      /**
       * TODO: Add reading the data from files and displaying it
       * Waiting for creation of JSONs
       */
      res.status(200).json({
        data: "Bon",
      });
    }
  );

  return distributions;
};
