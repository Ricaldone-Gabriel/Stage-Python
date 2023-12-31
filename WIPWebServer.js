const express = require("express");
const path = require("path");
const ejs = require("ejs");
const utils = require("./utils.js");
const app = express();
const port = 3000;
//const { exec } = require("child_process");
//const plotterPython = "Plotter.py";
//const graphicsRoutes = require("./graphics.js");

//
//  ---------       ----------
//  |  Web  | <---- | Python | <---- Term
//  | Server| ----> | Server | <---- Term
//  ---------       ----------
//  Quando il Web Server necessita dei plot nuovi, li richiede al server python

app.set("view engine", "ejs");
app.use("/", express.static(__dirname + "/views"));
app.set("views", path.join(__dirname, "views"));
//app.use("/grafico", graphicsRoutes);

app.get("/", (req, res) => {
  res.render("index.ejs");
});

const server = app.listen(port, () =>
  console.log(`Example app listening on port ${port}!`)
);

//Socket---------------------------------------------------------
const io = require("socket.io")(server);

io.on("connection", (socket) => {
  console.log("Un client si è connesso");
  setTimeout(() => {
    socket.emit("message", true);
  }, 2000);

  socket.on("Plot_answer", (data) => {
    console.log("Messaggio ricevuto:", data);
    //socket.emit("conferma", "Messaggio ricevuto con successo");
  });

  socket.on("disconnect", () => {
    console.log("Il client si è disconnesso");
  });
});
