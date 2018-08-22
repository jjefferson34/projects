
var saved = [];

function moveFunc(recipe){ //in the saved_results.html there is a button onclick that starts this
  //when button1 is clicked, move from result to saved
  var text = "";
  //document.getElementById("waffles").innerHTML = JSON.stringify(saved);
  //could work by making it a cookie
//  saved.push("<p>");
//saved.push("</p>");
text += "</p>" + "<p id='result'>" + " " + "<a href =" + recipe['url'] + ">" + recipe['name'] + "</a>";
  if (saved.includes(text) == false) {

    saved.push(text);

    document.getElementById("waffles").innerHTML = saved;
  }
}
