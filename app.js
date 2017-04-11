
var express = require('express');
var app = express();

app.get('/', function (req, res) {
  res.send('Hello World! I am an express app');
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
