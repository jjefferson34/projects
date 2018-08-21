// 2. This code loads the IFrame Player API code asynchronously.
      var tag = document.createElement('script');

      tag.src = "https://www.youtube.com/iframe_api";
      var firstScriptTag = document.getElementsByTagName('script')[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

      // 3. This function creates an <iframe> (and YouTube player)
      //    after the API code downloads.
      var player;
      function onYouTubeIframeAPIReady() {
        player = new YT.Player('player', {
          height: '390',
          width: '640',
          videoId: 'ypuaJLHK_LQ',
          //playerVars: { 'autoplay' : 1 },//
          events: {
            'onReady': onPlayerReady,
            //object.onclick = function(){myScript}//
          }
        });
      }
 //API will call this function when the video player is ready//
function onPlayerReady(event) {
  player.setVolume(75);
  //event.target.playVideo();//
}


function play() {
  player.playVideo();
}

function pause() {
  player.pauseVideo();
}

function stop() {
  player.stopVideo();
}


function video2() {
  player.loadVideoById("KaamZkadYvo", 0, "large");
}
 function video3() {
   player.loadVideoById("bdEF9WEiO5g", 0, "large");
 }

 function video4() {
  player.loadVideoById("wwyznoWJDHI", 0, "large");
 }
