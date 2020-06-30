/**
 * Production packages
 */
const express = require("express");
const config = require("./config.json");
const api = require("./api");
const db = require("./db");

/**
 * Dev packages
 */
if (process.env.ENV === "DEVELOPMENT") {
  const dotenv = require("dotenv");
  dotenv.config();
  const morgan = require("morgan");
  // Loggin of requests
  app.use(morgan("common"));
}

const app = express();

// Set json response header
app.use((req, res, next) => {
  req.headers["Content-Type"] = "application/json";
  next();
});

db.initDb({ config }, ({ config, db }) => {
  app.use("/api", api.getRouter({ config, db }));

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
