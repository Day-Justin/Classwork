const socket = io();
var form = document.getElementById('form');
var input = document.getElementById('input');
var messages = document.getElementById('messages');
const QC = {lat: 40.73637462858518, lng: -73.82047927629468};
var currentRoom = 'QC';
var newMarker;
var userMarkers = L.layerGroup([]);
var roomMarkers = L.layerGroup([]);
var PMs = {};
var pmTarget = '';
var togglePM = document.querySelector(".togglePM");
var nameText = document.getElementById("userNameText");
var curGroupText = document.getElementById("currentGroupText");

//Direct Message Box Toggle Button
togglePM.addEventListener("click", () => {
  let pmWindow = document.querySelector(".pmBox");
  if(pmWindow.style.display == "none" && pmTarget != ""){
    pmWindow.style.display = "flex";
    togglePM.innerText = ">"
    showPMchat(pmTarget);
  }
  else{
    pmWindow.style.display = "none";
    togglePM.innerText = "<"
  }
})

// Map:
var map = L.map('map',).setView(QC, 16.5);
map.on('click', addMarker);
document.getElementById('map').style.cursor = 'default'

// Add the base layer to map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


// Chat:
// Chat Submit Button
form.addEventListener('submit', function(e) {
  e.preventDefault();
  if (input.value) {
    let msg = input.value;
    socket.emit('chat message', {msg, currentRoom});
    input.value = '';
  }
});

// Initial Connection, Get Username and Group, Supply Dummy User Coordinates to Server
socket.on("connect", () => {
  nameText.innerText = socket.id;
  curGroupText.innerText = currentRoom;
  //Submit QC coords to server as client starting position until geolocation succeeds
  socket.emit('geoupdate', QC.lat, QC.lng, currentRoom); 
});

// Display Chat Message On Screen
socket.on('chat message', function(msg) {
    var item = document.createElement('li');
    item.innerHTML = `<b>${msg}</b>`;
    messages.appendChild(item);
    item.scrollIntoView();
    //window.scrollTo(0, item.scrollHeight);
  });

// Display PM Chat Message On Screen if window is open, else notifies recipient that a new message is recieved
socket.on('pm chat message', function(args) {
  //No record found, create new record
  if(!PMs[args.sid])
    PMs[args.sid] = `<li><i>Chatting with User ${args.sid}.</i></li>`;
  var item = `<li><b>${args.msg}</b></li>`;
  //Update record with new message
  PMs[args.sid] += item;
  //console.log(PMs[args.sid])

  //If User is the recipient of the Message
  if(socket.id != args.fid){
    // console.log(socket.id);
    // console.log(args.fid);
    var pBox = document.querySelector('.pmBox');
    // Checks if the PM window is open, else give notification of new message
    if(pBox.style.display == 'none' || (pBox.style.display == 'flex' && pmTarget != args.sid)) {
      PMs[args.sid + '_read'] = false;
      var row = document.getElementById(`${args.sid}`);
      row.style.backgroundColor = "red";
    }
    else {
      PMs[args.sid + '_read'] = true;
      var row = document.getElementById(`${args.sid}`);
      row.style.backgroundColor = "rgba(138, 138, 138, 0.15)";
    }
  }

  //Updates PM window with messages
  var pmBox = document.querySelector(".pmBox");
  var pmChat = document.getElementById('pm_messages');
  var pmForm = document.querySelector(".pm_form");
  if(pmBox.style.display == 'flex'){
    if(PMs[args.sid] && pmTarget == args.sid){
      pmChat.innerHTML = PMs[args.sid];
      pmChat.children[pmChat.children.length-1].scrollIntoView();
    }
    //Provide proper destination for current message in PM form
    pmForm.addEventListener('submit', function(e) {
      e.preventDefault();
      var pm_input = document.querySelector(".pm_input");
      if (pm_input.value) {
        let msg = pm_input.value;
        socket.emit('pm chat message', {uID: `${pmTarget}`, msg: `${msg}`});
        pm_input.value = '';
      }
    });
  }
    

});

// Display System Chat Message On Screen
socket.on('system chat message', function(msg) {
  var item = document.createElement('li');
  item.innerHTML = `<i style="color:gray">${msg}</i>`;
  messages.appendChild(item);
  item.scrollIntoView();
  //window.scrollTo(0, item.scrollHeight);
});


// Updates Rooms List
socket.on('roomsUpdate', function(msg) {
  var roomList = document.getElementById('room-list');
  roomList.innerHTML = `<tbody id="room-table"></tbody>`;
  var roomTable = document.getElementById('room-table');
  //console.log(msg);
  var rooms = [];
  var curRoomMarker;

  for (let [key, value] of Object.entries(msg)) {
    //console.log(`${key}: ${value}`);
    //Room Marker Update
    let roomMarker = new L.circleMarker([value.lat, value.lng]);
    //QC is the only group with no marker
    if(key != 'QC'){
      //console.log(roomMarker);
      if(key == currentRoom){
        roomMarker.bindPopup(`
        <h3>Group:</br> ${key}</h3>
        <button id="${key}-btn2" class="listBtn" style="color: gray" disabled="true">Joined</button>`,     
        {
          //permanent: true,
          direction: 'top',
          className: 'roomLabels joinedRoomPopup'
        });

        roomMarker.bindTooltip(`
          <div class="roomMarkerBelow">
            <h2>${key}</h2>
            <h3><i>(Joined)</i></h3>
          </div>`,     
          {
            permanent: true,
            direction: 'bottom',
            className: 'roomLabels joinedRoomTooltip'
          });
      }
      //For All Other Room Markers and Tooltips
      else{
        roomMarker.bindPopup(`
          <h3>Group:</br> ${key}</h3>
          <button id="${key}-btn2" class="listBtn" onclick="joinBtnHandler('${key}')">Join</button>`,     
          {
            //permanent: true,
            direction: 'top',
            className: 'roomLabels roomPopup'
          });
      
        roomMarker.bindTooltip(`
          <div class="roomMarkerBelow">
            <h2>${key}</h2>
          </div>`,     
          {
            permanent: true,
            direction: 'bottom',
            className: 'roomLabels roomTooltip'
          }
        );
      }
      roomMarker.on("mouseover", () => {
        roomMarker.openPopup();
        setTimeout(() => {
          roomMarker.closePopup();
        }, 6000);
        
      });
      rooms.push(roomMarker);
    }

    //Group List Row Update
    let roomRow = document.createElement("tr");
    roomRow.addEventListener("click", () => {
      map.flyTo([value.lat, value.lng]);
      if(roomMarker != null)
        roomMarker.openPopup();
        setTimeout(() => {
          roomMarker.closePopup();
        }, 6000);
    });

    let entry = document.createElement("td");
    entry.classList.add("roomCell");
    entry.innerText = key;
    let btnCell = document.createElement("td");
    let btn = document.createElement("button");
    btn.classList.add("listBtn");
    btn.id = key + "-btn";
    btn.textContent = "Join";

    if(key == currentRoom){
      entry.style.color = 'rgb(150, 0, 150)';
      //btn.style.display = 'none';
      btn.style.color = "gray";
      btn.textContent = "Joined";
      btn.disabled = true;
      if(key != 'QC')
        curRoomMarker = roomMarker;
    }
    btn.addEventListener("click", () =>{
      joinBtnHandler(key);
    });

    roomRow.appendChild(entry);
    btnCell.appendChild(btn);
    roomRow.appendChild(btnCell);
    roomTable.appendChild(roomRow);
  }

  //Refresh all markers and Update
  map.removeLayer(roomMarkers);
  roomMarkers = L.layerGroup(rooms);
  roomMarkers.addTo(map);
  //console.log(roomMarkers);
  if(curRoomMarker != null)
    curRoomMarker._path.classList.add("currentRoomMarker");
});

// Join Button Handler Function
function joinBtnHandler(key) {
  //console.log(key);
  //console.log(currentRoom);
  socket.emit('leaveRoom', currentRoom);
  messages.innerHTML = ``;
  currentRoom = key;
  socket.emit('joinRoom', key);
  curGroupText.innerText = currentRoom;
  document.querySelector(".pmBox").style.display = "none";
};

// Updates Users List
socket.on('usersUpdate', function(msg) {
  var userList = document.getElementById('user-list');
  userList.innerHTML = `<tbody id="user-table"></tbody>`;
  var userTable = document.getElementById('user-table');
  var users = [];
  var myMarker;
  var pmTargetActive = false;

  for (let [key, value] of Object.entries(msg)) {
    //console.log(`${key}: ${value}`);
    //User Marker Update
    let userMarker = new L.marker([value.lat, value.lng]);
    userMarker.uID = key;
    userMarker.bindTooltip(key, 
      {
          //permanent: true,
          direction: 'top',
          className: 'userLabels'
      });
    
    let pmPopup = document.createElement("div");
    pmPopup.style.display = "flex";
    pmPopup.style.flexDirection = "column";
    let pmBanner = document.createElement("h2");
    pmBanner.innerText = key;
    pmPopup.appendChild(pmBanner);
    let popupPMbtn = document.createElement("button");
    popupPMbtn.classList.add("listBtn");
    popupPMbtn.innerText = "Direct Message";
    popupPMbtn.addEventListener("click", () =>{
      togglePM.style.display = "flex";
      togglePM.innerText = ">";
      showPMchat(key); 
      userMarker.closePopup();
    });
    pmPopup.appendChild(popupPMbtn);

    if(key != socket.id)
      userMarker.bindPopup(pmPopup);

    userMarker.on("mouseover", () => {
      if(key == socket.id)
        userMarker._icon.src = "/map/images/marker-icon-violet.png";
      else
        userMarker._icon.src = "/map/images/marker-icon-red.png";
    });
    userMarker.on("mouseout", () => {
      if(key == socket.id)
        userMarker._icon.src = "/map/images/marker-icon-gold.png";
      else
        userMarker._icon.src = "/map/images/marker-icon-blue.png";
    });

    //User List Row Update
    let rowEntry = document.createElement("tr");
    rowEntry.id = `${key}_listrow`;
    let entry = document.createElement("td");
    entry.id = `${key}`;
    entry.innerText = key; 
    let pmBtnDiv = document.createElement("div");
    let pmBtn = document.createElement("button");
    pmBtn.classList.add("listBtn");
    pmBtn.innerText = "Direct Message";

    pmBtn.addEventListener("click", () => {
      let pmWindow = document.querySelector(".pmBox");
      togglePM.style.display = "flex";
      togglePM.innerText = ">";
      if(key == pmTarget && pmWindow.style.display == "flex"){
        togglePM.innerText = "<";
        pmWindow.style.display = "none";
      }
      else{
        showPMchat(key); 
      }
    })
    rowEntry.addEventListener("click", () => {
      map.flyTo([value.lat, value.lng]); 
    })
    rowEntry.addEventListener("mouseover", ()=>{
      userMarker.openTooltip();
      if(key == socket.id)
        userMarker._icon.src = "/map/images/marker-icon-violet.png";
      else
        userMarker._icon.src = "/map/images/marker-icon-red.png";
    })
    rowEntry.addEventListener("mouseout", ()=>{
      userMarker.closeTooltip();
      if(key == socket.id)
        userMarker._icon.src = "/map/images/marker-icon-gold.png";
      else
        userMarker._icon.src = "/map/images/marker-icon-blue.png";
    })

    if(key == socket.id){
      entry.style.color = 'rgb(150, 0, 150)';
      myMarker = userMarker;
    }
    else if (PMs[key] && PMs[key + '_read'] == false) {
        entry.style.backgroundColor = "red";
    }
    users.push(userMarker);

    if(key == pmTarget){
      pmTargetActive = true;
    }

    pmBtnDiv.appendChild(pmBtn);
    rowEntry.appendChild(entry);
    if(key != socket.id)
      rowEntry.appendChild(pmBtnDiv);
    userTable.appendChild(rowEntry);
    //console.log(PMs[key + '_read']);
  }

  if(!pmTargetActive){
    document.querySelector(".pmBox").style.display = "none";
    pmTarget = "";
    togglePM.style.display = "none";
  }
  map.removeLayer(userMarkers);
  userMarkers = L.layerGroup(users).addTo(map);

  //Color User Marker
  if (myMarker != null){
    myMarker._icon.src = "/map/images/marker-icon-gold.png";
  }

});


//Opens PM window with target
function showPMchat(key){
  pmTarget = key;
  //console.log(pmTarget);
  var entry = document.getElementById(`${pmTarget}`);
  entry.style.backgroundColor = "rgba(138, 138, 138, 0.15)";
  var pmBox = document.querySelector(".pmBox");
  var pmChat = document.getElementById('pm_messages');
  var pmForm = document.querySelector(".pm_form");

  if(pmTarget != socket.id){
    pmBox.style.display = 'flex';
    pmChat.innerHTML = `<li><i>Chatting with User ${pmTarget}.</i></li>`;
    if(PMs[pmTarget]){
      pmChat.innerHTML = PMs[pmTarget];
      pmChat.children[pmChat.children.length-1].scrollIntoView();
      PMs[pmTarget + '_read'] = true;
    }
    pmForm.addEventListener('submit', function(e) {
      e.preventDefault();
      var pm_input = document.querySelector(".pm_input");
      if (pmTarget && pm_input.value) {
        let msg = pm_input.value;
        socket.emit('pm chat message', {uID: `${pmTarget}`, msg: `${msg}`});
        pm_input.value = '';
      }
    });
  }
  else{
    pmChat.innerHTML = ``;
    pmBox.style.display ='none';
  }


}

//Sends PM to a user
function sendPM(uID){
  //Awaits PM window element
  //console.log(uID)
  var elementExist = setInterval(() => {
    var pmForm = document.querySelector(`.pm_form`);
    if(pmForm != null){
      pmForm.addEventListener('submit', function(e) {
        e.preventDefault();
        var pm_input = document.querySelector(`.pm_input`);
        if (pmTarget && pm_input.value) {
          let msg = pm_input.value;
          socket.emit('pm chat message', {uID: `${uID}`, msg: `${msg}`});
          pm_input.value = '';
        }
      });
      clearInterval(elementExist);
    }
  }, 100);
}

// Map Marker Functions:
// Adds marker to map for group creation
function addMarker(e){
  if(newMarker != null)
    map.removeLayer(newMarker);
  // Add marker to map at click location;
  newMarker = new L.circleMarker(e.latlng).addTo(map);
  newMarker._path.classList.add("pendingGroup");
  // Add a popup to the marker, includes group creation form HTML
  newMarker.bindPopup(`
    <div class="groupCreateForm">
      <h2>New Group Creation<h2>
      <form id="room-form">
        <input type="text" id="room-input" autocomplete="off" required>
        <button>Create</button>
      </form>  
    </div>`).openPopup();

  const roomForm = document.getElementById('room-form');
  
  // Event listener for room creation form
  roomForm.addEventListener('submit', (event) => {
    map.removeLayer(newMarker);
    event.preventDefault();
    const roomInput = document.getElementById('room-input');
    const roomName = roomInput.value;
    socket.emit('leaveRoom', currentRoom);
    document.querySelector(".pmBox").style.display = "none";
    messages.innerHTML = ``;
    currentRoom = roomName;
    curGroupText.innerText = currentRoom;
    let roomCoords = newMarker.getLatLng();
    socket.emit('createRoom', {roomName, roomCoords});
    roomInput.value = '';
  });

  newMarker.on('click', ()=> {
    map.removeLayer(newMarker);
  });
}

//GeoLocation:
//When GeoLocation Succeeds
function success(pos) {
  const crd = pos.coords;
  //Once geolocation is successful, emit to server for updating
  socket.emit('geoupdate', crd.latitude, crd.longitude, currentRoom); 
}

//Error thrown for GeoLocation
function error(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
}

//Options for GeoLocation- High accuracy, 10s to return location before timeout, update every 1s
const options = {
  enableHighAccuracy: true,
  timeout: 10000,
  maximumAge: 1000
};

//Updates position on movement, Watch Position requires HTTPS on some/all browsers
navigator.geolocation.watchPosition(success, error, options);