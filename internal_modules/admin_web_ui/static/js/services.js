function manage_power(type)
{
var xmlhttp = new XMLHttpRequest();
var url = location.protocol + "//" + location.hostname + ":" + location.port + '/admin/power?control='+type;

xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        alert(myArr.msg);
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send();

}

function manage_ssh(state)
{
var xmlhttp = new XMLHttpRequest();
var url = location.protocol + "//" + location.hostname + ":" + location.port + '/admin/ssh?state='+state;

xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        alert(myArr.msg);
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send();
}
