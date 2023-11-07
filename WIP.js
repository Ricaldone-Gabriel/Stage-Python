const express = require("express");
const { exec } = require("child_process");
const path = require("path");
const ejs = require("ejs");
const utils = require("./utils.js");
const plotterPython = "Plotter.py";
const app = express();
const port = 8080;
//const graphicsRoutes = require("./graphics.js");

//
//  ---------       ----------
//  |  Web  | <---- | Python | <---- Term
//  | Server| ----> | Server | <---- Term
//  ---------       ----------
//
//  Quando il Web Server necessita dei plot nuovi, li richiede al server python

app.set("view engine", "ejs");
app.use("/", express.static(__dirname + "/views"));
app.set("views", path.join(__dirname, "views"));
//app.use("/grafico", graphicsRoutes);

app.get("/", (req, res) => {
  res.render("index.ejs");
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));

exec(`python ${plotterPython}`, (err) => {
  if (err) {
    console.log(err);
    return;
  } else {
    console.log("Avviato");
  }
});
