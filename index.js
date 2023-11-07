const express = require("express");
const path = require("path");
const ejs = require("ejs");
const utils = require("./utils.js");
const app = express();
const port = 8080;
//const graphicsRoutes = require("./graphics.js");

app.set("view engine", "ejs");
app.use("/", express.static(__dirname + "/views"));
app.set("views", path.join(__dirname, "views"));
//app.use("/grafico", graphicsRoutes);

app.get("/", (req, res) => {
  res.render("index.ejs");
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
