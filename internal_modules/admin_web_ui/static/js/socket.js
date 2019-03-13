function CreateNewWindow(name)
{
   container = document.getElementById('text_output');
   title = document.createElement('label');
   title.for = 'name';
   title.style = 'display:block; text-align: center;';
   bold = document.createElement('b');
   bold.innerHTML = name + ':';
   title.appendChild(bold);
   new_elem = document.createElement('textarea');
   new_elem.id = name;
   new_elem.rows = "5";
   new_elem.cols = "60";
   new_elem.disabled = true;
   new_elem.readonly = true;
   new_elem.style = "resize: none; text-align: center; display:block;";
   td = document.createElement('td');
   td.appendChild(title);
   td.appendChild(new_elem);
   
   last_tr = container.childNodes[container.childNodes.length - 1];
   if(last_tr.childElementCount >= 3) {
   container.appendChild(document.createElement('tr')); }
   
   container.childNodes[container.childNodes.length - 1].appendChild(td);
}

socket = io.connect(location.protocol + "//" + location.hostname + ":" + location.port + '/websocket');

socket.on('connect', function () { console.log("Connected to websocket !!"); });

socket.on('update_tp', function (msg) {
   console.log("Received from server : " + msg);
   data = JSON.parse(msg);
   console.log(data);
   tp_name = data.topic_name;
   msg_data = data.msg;
   document.getElementById(tp_name).innerHTML = document.getElementById(tp_name).innerHTML + '\n' + msg_data;
     });

socket.on('get_tplist', function (msg) {
   console.log("Received from server : " + msg);
   tplist = JSON.parse(msg);
   console.log(tplist);
   for (i = 0; i < tplist.length; i++) { 
  CreateNewWindow(tplist[i]);
  }
     });
