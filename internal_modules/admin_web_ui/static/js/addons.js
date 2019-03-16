function CreateNewAddon(addon)
{
   container = document.getElementById('table_body');
   tr = document.createElement('tr');
   td_name = document.createElement('td');
   td_date = document.createElement('td');
   td_token = document.createElement('td');
   td_email = document.createElement('td');
   td_name.innerHTML = addon.name;
   td_email.innerHTML = addon.email;
   td_token.innerHTML = addon.token;
   td_date.innerHTML = addon.created_date;
   td_name.style = "border: 1px solid #333;";
   td_date.style = "border: 1px solid #333;";
   td_email.style = "border: 1px solid #333;";
   td_token.style = "border: 1px solid #333;";
   
   td_suppr = document.createElement('td');
   button_suppr = document.createElement('button');
   button_suppr.type = "button";
   button_suppr.innerHTML = "Delete this addon";
   button_suppr.addEventListener("click", function() {delete_addon(addon.token);});

   td_suppr.appendChild(button_suppr);

   tr.appendChild(td_name);
   tr.appendChild(td_email);
   tr.appendChild(td_date);
   tr.appendChild(td_token);
   tr.appendChild(td_suppr);

  container.appendChild(tr);
}


function delete_addon(token)
{
var xmlhttp = new XMLHttpRequest();
var url = location.protocol + "//" + location.hostname + ":" + location.port + '/admin/addons/manage?token='+token;
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
	refresh_addon();
	alert(myArr.msg);
    }
};
xmlhttp.open("DELETE", url, true);
xmlhttp.send();
}

function refresh_addon()
{
var xmlhttp = new XMLHttpRequest();
var url = location.protocol + "//" + location.hostname + ":" + location.port + '/admin/addons/manage';
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        console.log(myArr);
	if(myArr.code == "success") {
	var myNode = document.getElementById("table_body");
	while (myNode.firstChild) { myNode.removeChild(myNode.firstChild); }
	for(var i =0; i < myArr.msg.length; i++) { CreateNewAddon(myArr.msg[i]);	}
	}
	else {
        alert(myArr.msg);}
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send();
}


function create_addon()
{
var xmlhttp = new XMLHttpRequest();
var url = location.protocol + "//" + location.hostname + ":" + location.port + '/admin/addons/manage';
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        refresh_addon();
        alert(myArr.msg);
    }
};
form = document.getElementById('new_form');
console.log(form);
xmlhttp.open("POST", url, true);
xmlhttp.send(new FormData(form));
}

refresh_addon();
