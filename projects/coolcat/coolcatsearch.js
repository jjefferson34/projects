var key = localStorage.getItem("query");

function results() {
  console.log("hi");
  localStorage.query = document.getElementById("input").value;
  var key = localStorage.getItem("query");

  //window.open("catsaved.html");
  window.open("https://www.allrecipes.com/search/results/?wt=" + key + "&sort=re");
}

/*
"https://www.allrecipes.com/search/results/?wt=" + key + "&sort=re";
"https://cooking.nytimes.com/search?q=" + key;
"https://www.epicurious.com/search/" + key;
"https://www.tablespoon.com/search?term=" + key + "&termDataSource=d6fb75f5-d19a-49cd-9ba0-c10a6e45afb2";
"https://smittenkitchen.com/?s=" + key;

if () {

"https://www.foodnetwork.com/search/" + key + "-"
}

else {
  "https://www.foodnetwork.com/search/" + key + "-"
}
 */
