const express = require("express");
const app = express();
const js = require("./data/data.json");

app.use(express.static("static"));
app.get("/data", (req, res) => {
  res.send(js);
});

var port = process.env.PORT || 3000;
app.listen(port, function () {
  console.log(
    "To view your app, open this link in your browser: http://localhost:" + port
  );
});
