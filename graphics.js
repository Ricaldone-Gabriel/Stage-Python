const express = require("express");
const path = require("path");
const ejs = require("ejs");
const app = express();
const graphicsRoutes = express.Router();
const port = 8080;

app.set("view engine", "ejs");
graphicsRoutes.use(express.static(__dirname + "/plots"));

graphicsRoutes.get("/recente", (req, res) => {
  res.render("../Plots/2023-11-02.html");
});

module.exports = graphicsRoutes;
