(function() {
  var cx = '013963066909738430103:a1gjjmqycxc';
  var gcse = document.createElement('script');
  gcse.type = 'text/javascript';
  gcse.async = true;
  gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
  var s = document.getElementsByTagName('script')[0];
  s.parentNode.insertBefore(gcse, s);
})();

console.log(gcse);
console.log(q);

//var query = input that i need to source from search box if psosible
//GET "https://www.googleapis.com/customsearch/v1?key=AIzaSyAd7gLsn4yFpi7EVFHyKVfurdFVekz9m7o&cx=013963066909738430103:a1gjjmqycxc&q=" + input


//search engine id: 013963066909738430103:a1gjjmqycxc
//api key:AIzaSyAd7gLsn4yFpi7EVFHyKVfurdFVekz9m7o

<script src="https://apis.google.com/js/api.js"></script>
    <script>
      function start() {
        gapi.client.init({
          'apiKey': 'AIzaSyAd7gLsn4yFpi7EVFHyKVfurdFVekz9m7o',
          'discoveryDocs': ['https://www.googleapis.com/customsearch/v1?'],
        }).then(function() {
          // Executes an API request, and returns a Promise.
          // The method name `language.translations.list` comes from the API discovery.
          return gapi.client.language.translations.list({
            q: 'hello world',
            source: 'en',
            target: 'de',
          });
        }).then(function(response) {
          console.log(response.result.data.translations[0].translatedText);
        }, function(reason) {
          console.log('Error: ' + reason.result.error.message);
        });
      };

      // Loads the JavaScript client library and invokes `start` afterwards.
      gapi.load('client', start);
    </script>
