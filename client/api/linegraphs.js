const express = require("express");
const Validator = require("validatorjs");

exports.getRouter = ({ config, db }) => {
  const lc = express.Router();

  lc.get("/procentaj-alegere-s3/:section/:area", (req, res) => {
    req.params.subfolder = "procentaj-alegere-s3";

    /**
     * Validating correct URL parameters
     */
    const validationRules = {
      subfolder: ["string", "alpha_dash"],
      subject: ["string", "alpha_dash"],
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
      section: ["in:filologie,mate-info,stiinte-ale-naturii,tehnic"],
      area: [
        "in:anatomie,biologie,chimie-anorganica,chimie-organica,fizica,informatica",
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

    const { error, data } = db.getLineChart(params);

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

  lc.get("/:subfolder/:area", (req, res) => {
    /**
     * Validating correct URL parameters
     */
    const validationRules = {
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
      subfolder: ["in:evolutie-medie,evolutie-promovabilitate"],
      area: [
        "in:filiera-tehnologica-si-tehnica,filologie,mate-info,stiinte-sociale,stiinte-ale-naturii,zona-rurala,zona-urbana",
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

    const { data, error } = db.getLineChart(params);

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

  return lc;
};
