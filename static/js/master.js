window.addEventListener('click', filter, false);
var spin = document.getElementsByClassName("spin");
var socket;
var network = document.createElement("h1");
network.innerHTML = "<br><br>Интернета нет<br>или сайт полёг"

function filter(e){
  if (e.target.tagName === 'A'){ // провека что кликнули на ссылку
    console.log(e.target.href);  // получаем URL адрес ссылки
    e.preventDefault();          // отменяем переход
    spin[0].style.display = "flex";
    window.location.href = e.target.href; // переходите по ссылке
  }
}

// var socket = io.connect('//' + document.domain + ':' + location.port);
// socket.on('message', function(msg){alert("123");} );
// socket.onAny(function(msg){alert("123");})

function showMsg(msgs) {
  window.location.reload();
        // var i, domStreamNew;
        // for (i = 0; i < msgs.length; ++i) {
            // alert(msgs[i]);
        // }
    }

function netErrs(msgs) {
  var load = document.getElementById("load");
  var page = document.getElementById("date_list");
  load.style.display = "none";
  page.append(network);
}

function initSocketIO() {
  socket = io.connect('//' + document.domain + ':' + location.port);
  socket.on('show-msg', showMsg);
  socket.on('netErr', netErrs)
  // socket.onAny('show-msg', showMsg);
  // socket.on('connect', function() {
  socket.emit('request-all-msgs');
  // });
}

initSocketIO();
