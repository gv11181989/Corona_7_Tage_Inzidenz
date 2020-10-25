//Server code start
const port = process.env.PORT || 3000;
const express = require('express');
const app = express();
var graphArray = []
var server = app.listen(port, () => {
  console.log("port 3000 active");
});

app.use(express.static('./public'));
//Server code end


//Import from python start
let { PythonShell } = require('python-shell');
var options = {
  scriptPath: './',
  args: [],
  mode: "json"
};

let pyshell = new PythonShell('db.py', options);
pyshell.on('message', function cal(message) {
  
  var pythonData = message;
//Import from python end 
  graphArray = pythonData
  console.log(graphArray);
  
const socket = require('socket.io');
const io = socket(server);
io.sockets.on('connection', (socket) => {
  setInterval(() => {
    console.log(socket.id);
    console.log(graphArray);
    socket.broadcast.emit('graphArray', graphArray);
  }, 60000);
});

});



