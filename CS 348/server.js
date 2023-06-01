const path = require('path');
const fs = require('fs');
const express = require('express');
const https = require('https');
const app = express();
const socket = require("socket.io");
const port = 3000;
const qcGlobal = 'QC';
const qcCoords = {lat: 40.73637462858518, lng: -73.82047927629468};
const rooms = {};
rooms.QC = qcCoords;

// Default Route Hndler
app.get('/', (req, res) => {
    console.log("Incoming GET Request From: " + req.ip + ", Sending Static Files...");
    res.sendFile(path.join(__dirname + '/public/index.html'));
});

// Key location for self-signed cert
const sslKeys = {
  key: fs.readFileSync('server.key'), 
  cert: fs.readFileSync('server.cert')
};

// Creates HTTPS server
const server = https.createServer(sslKeys, app).listen(port, () => {
  console.log(`Express server listening on port: ${port}!`);
});

//Listens for Socket Connection over HTTP(S) server
const io = socket(server);

// Socket Handler Functions
io.on('connection', (socket) => {
    io.emit('system chat message', socket.id + ' Connected.');
    console.log("New Socket Connection: " + socket.request.connection.remoteAddress + " -> Assigned User ID: " + socket.id);
    // Client joins default 'Global' channel on connection
    socket.join(qcGlobal);
    //console.log(io.sockets.adapter.rooms);
    
    //Emit User List to room
    if(io.sockets.adapter.rooms.get(qcGlobal)){
      setTimeout(() => {
        let roomUsers = {};
        io.sockets.adapter.rooms.get(qcGlobal).forEach(user => {
          roomUsers[user] = socket.coords;
          //console.log(socket.coords);
        });
        io.to(qcGlobal).emit('usersUpdate', roomUsers);
      }, 500);
    }

    //Emit Room list to all
    io.emit('roomsUpdate', rooms);
    
    io.to(qcGlobal).emit('system chat message', socket.id + ' Connected to: ' + qcGlobal + '.');
    console.log('User ' + socket.id + ' Connected to ' + qcGlobal + '.');

    // Client Sending Messages
    socket.on('chat message', (args) => {
      io.to(args.currentRoom).emit('chat message', socket.id + ': ' + args.msg);
      });

    //Client Sending PM to another User
    socket.on('pm chat message', (args) => {
      //console.log(args);
      io.to(args.uID).emit('pm chat message', {fid: `${socket.id}`,  sid: `${socket.id}`, msg: socket.id + ': ' + args.msg});
      io.to(socket.id).emit('pm chat message', {fid: `${socket.id}`, sid: `${args.uID}`, msg: socket.id + ': ' + args.msg});
    });

    // Handle room creation
    socket.on('createRoom', (args) => {
      let roomName = args.roomName;
      let roomCoords = args.roomCoords;

      if(!io.sockets.adapter.rooms.get(roomName) && roomName != qcGlobal){
         // Create a new room
        socket.join(roomName);
        io.to(roomName).emit('system chat message', socket.id + ' Connected to: ' + roomName + '.');
        console.log(`User ${socket.id} Connected to: ${roomName}.`);
        // Update Room coords
        rooms[roomName] = roomCoords;
      }
      else{
        //Join Room
        socket.join(roomName);
        io.to(socket.id).emit('system chat message', 'Group: ' + roomName + ' Already Exists. Joining Existing Room...');
        io.to(roomName).emit('system chat message', socket.id + ' Connected to: ' + roomName + '.');
        console.log(`User ${socket.id} Connected to: ${roomName}.`);
      }

      //Emit Room list to all
      io.emit('roomsUpdate', rooms);
      //console.log(rooms);

      //Emit User List to room 
      let roomUsers = {};
      //console.log(io.sockets.adapter.rooms.get(roomName));
      io.sockets.adapter.rooms.get(roomName).forEach(user => {
        roomUsers[user] = io.sockets.sockets.get(user).coords;
      });
      io.to(roomName).emit('usersUpdate', roomUsers);
      //console.log(roomUsers);

    });

    socket.on('joinRoom', (roomName) => {
      //Join Room
      //io.sockets.adapter.rooms.get(roomName).has(socket.id);
      socket.join(roomName);
      io.to(roomName).emit('system chat message', socket.id + ' Connected to: ' + roomName + '.');
      console.log(`User ${socket.id} Connected to: ${roomName}.`);
      //console.log(rooms);
      
      //Emit User List to room 
      let roomUsers = {};
      io.sockets.adapter.rooms.get(roomName).forEach(user => {
        roomUsers[user] = io.sockets.sockets.get(user).coords;
      });
      io.to(roomName).emit('usersUpdate', roomUsers);

      //Emit Room list to all
      io.emit('roomsUpdate', rooms);
    });

    //Leave Current Room
    socket.on('leaveRoom', (roomName) => {      
      socket.leave(roomName);
      if((!io.sockets.adapter.rooms.get(roomName) || io.sockets.adapter.rooms.get(roomName).size == 0) && roomName != qcGlobal){
        delete rooms[roomName]; 
        //Emit Room list to all **
        io.emit('roomsUpdate', rooms);
      }
      else if(io.sockets.adapter.rooms.get(roomName) && io.sockets.adapter.rooms.get(roomName).size > 0){
        io.to(roomName).emit('system chat message', `${socket.id} Has Left The Room.`);
        console.log(`User ${socket.id} Left Room: ${roomName}.`);
        //Emit User List to room 
        let roomUsers = {};
        io.sockets.adapter.rooms.get(roomName).forEach(user => {
          roomUsers[user] = io.sockets.sockets.get(user).coords;
        });

        io.to(roomName).emit('usersUpdate', roomUsers);
      }
      

    });

    //Client Disconnection
    socket.on('disconnect', () => {
      io.emit('system chat message', socket.id + ' Disconnected.');
      console.log('User ' + socket.id + ' @ ' + socket.request.connection.remoteAddress +' Disconnected.');
      
      for(let roomName in rooms){
        if(io.sockets.adapter.rooms.get(roomName) && io.sockets.adapter.rooms.get(roomName).size > 0){
          //io.to(roomName).emit(`User ${socket.id} Left The Room.`);
          console.log(`User ${socket.id} Left Room:${roomName}.`);
          //Emit User List to room 
          let roomUsers = {};
          io.sockets.adapter.rooms.get(roomName).forEach(user => {
            roomUsers[user] = io.sockets.sockets.get(user).coords;
          });
  
          io.to(roomName).emit('usersUpdate', roomUsers);
        }
      
        //Emit Room list to all **
        if((!io.sockets.adapter.rooms.get(roomName) || io.sockets.adapter.rooms.get(roomName).size == 0) && roomName != qcGlobal){
          delete rooms[roomName]; 
          io.emit('roomsUpdate', rooms);
        }
      }
      
    });


    
    //Client Geoupdates for server
    socket.on('geoupdate', (latitude, longitude, currentRoom) => {
        userCoords = {lat: `${latitude}`, lng: `${longitude}`};
        // console.log(socket.coords);
        // console.log(userCoords);
        if(!socket.coords || (socket.coords.lat != userCoords.lat && socket.coords.lng != userCoords.lng)){
          socket.coords = userCoords;
          console.log("User " + socket.id + " Coordinate Update-\tLat: " + socket.coords.lat + "\tLong: " + socket.coords.lng);
          //io.to(currentRoom).emit('userGeoUpdate', socket.id, userCoords)
          let roomUsers = {};
          if(io.sockets.adapter.rooms.get(currentRoom))
            io.sockets.adapter.rooms.get(currentRoom).forEach(user => {
                roomUsers[user] = io.sockets.sockets.get(user).coords;
            });
  
          //console.log(roomUsers);
          io.to(currentRoom).emit('usersUpdate', roomUsers);
        }
    });

  });

app.use(express.static(path.join(__dirname, '/public')));