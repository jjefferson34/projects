//document.cookie = "url = " + "green; expires=Thu, 18 Dec 2020 12:00:00 UTC;"

/*function setCookie(cname, cvalue, exdays) {
  //alert("setting cookie")
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + "," + expires + ",path=/";
}*/

function getCookie(cname) {
    //alert("getting cookie")
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(',');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}


function checkCookie() {
    var user=getCookie("username"); //HERE IS THE PROBLEM
    if (user != "") {
        alert("Welcome again " + user);
    } else {
       user = prompt("Please enter your name:","");
       if (user != "" && user != null) {
           //setCookie("username", user, 30);
           document.cookie = "username=" + user;
       }
    }
}
