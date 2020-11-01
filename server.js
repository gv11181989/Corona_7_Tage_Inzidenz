//Server code start

const port = process.env.PORT || 3000;
const express = require('express');
const app = express();
var graphArray = [];
var server = app.listen(port, () => {
  console.log("port 3000 active");
});

app.use(express.static('./public'));
//Server code end


//Import from python start
let { PythonShell } = require('python-shell');
var options = {
  pythonPath: 'python',
  scriptPath: './',
  args: [],
  mode: "json"
};


const socket = require('socket.io');
const io = socket(server);
io.sockets.on('connection', (socket) => {
  socket.on('from_client', function (data) {
    //console.log(data);
    let pyshell = new PythonShell('main.py', options);
    pyshell.send(data);
    pyshell.on('message', function (message) {
      graphArray = message;
      //setInterval(() => {
      //  console.log(socket.id);
      console.log(graphArray);
      socket.emit('graphArray', graphArray);
      //}, 6000);
      // end the input stream and allow the process to exit

    });
    pyshell.end(function (err) {
      if (err) {
        console.log( err);
      };
      console.log('finished')
    });
  });
});




