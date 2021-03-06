/**
 * Production packages
 */
const express = require("express");
const mongoose = require("mongoose");
const config = require("./config.json");
const api = require("./api");
const db = require("./db");

/**
 * Dev packages
 */
const dotenv = require("dotenv");
dotenv.config();
const morgan = require("morgan");

const app = express();

// Set json response header
app.use((req, res, next) => {
  req.headers["Content-Type"] = "application/json";
  next();
});

// Loggin of requests
app.use(morgan("common"));

db.initDb({ config }, ({ config, db }) => {
  /** Api endpoint */
  app.use("/api", api.getRouter({ config, db }));

  /** React build static files */
  app.use("/", express.static("frontend/build"));

  /** 404 Route, allways keep last */
  app.use("*", (req, res, next) => {
    res.status(404).json({
      error: {
        code: 404,
        msg: "Content not found",
        description:
          "We don't know what you are looking for, but make sure the URL is correct",
      },
    });
  });

  app.listen(process.env.PORT || config.port, () => {
    console.log(`Server listening on port ${process.env.PORT || config.port}`);
  });
});
