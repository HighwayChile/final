#!python

# This file containing the html must be in a cgi-bin sub-directory.

import cgi
import cgitb


print("content-type: text/html \n")
# main body of html
print("""
      
<!DOCTYPE html>
<html lang="en-US">
<head>
  <title>Dogesplorer</title>
  <link type="text/css" rel="stylesheet" href="/css/styles_final.css?version=1">

  <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
  <meta charset="UTF-8">
  <meta name="description" content="Doge Blockhain explorer">
  <meta name="keywords" content="doge, crypto, cryptocoin, cryptocurrency, 
  blockchain, block, wallet, address, addres, adress, explorer, explore, 
  search, dogecoin, coin, dog, dogcoin, shiba, inu, shib, sheeb, cheems, bonk,
  litecoin, ltc, trade, trades, trading, hash, transaction, bork, much, money,
  such, currency">
  <meta name="author" content="Dickie">
  <meta name="viewport" content="width=device-width, initial scale=1.0">
</head>

<body>
  <h1>Dogesplorer, the number one Doge explorer on the net!</h1>
    <!-- nav stuff (links and search) -->
    <nav class="main_nav">
      <div id="nav_links">
        <ul class="nav_list">
          <li><a href="/dir/sitemap.html">sitemap</a></li>
          <li><a href="/dir/dogegraph.html">graph</a></li>
          <li><a href="/dir/help.html">help</a></li>
          <li><a href="https://www.youtube.com/watch?v=Zfr3L0drhS8">link</a></li>
          <li><a href="https://www.youtube.com/watch?v=C3rg4psdHxw">link</a></li>
        </ul>
      </div>

      <form id="search_form">
        <input id="search_field" type="text" placeholder=" Enter a wallet address, txn hash, or contract address">
        <button id="search_btn" type="submit">search</button>
      </form>
    </nav>

    <!-- API shows Doge price here -->
    <div class="price_display">
      <div id="doge_tag"><h3>Doge Price: </h3></div>
      <div id="doge_price">Finding latest price...</div>
    </div>
      
    <br>
      
    <!-- API shows NASA daily photo here -->
    <div id="notify_display"><h4>NASA Astronomy Picture of the Day</h4></div>
    <div id="NASA-container">
        <!-- image spot -->
        <img width="100%" id="NASA-image" src="" alt="NASA APOD PICTURE MISSING">
        <!-- title and explanation right under! -->
        <p id="NASA-title"></p>
        <p id="NASA-explanation"></p>
    </div>


      <br><br><br><br><br><br><br>
     
""")




# form input for saved text message
cgitb.enable(display=0,logdir="/var/www/cgi-bin/error-logs")
file_path = "user_message.txt"
form = cgi.FieldStorage()
user_input: str = form.getvalue("user_input", "")
with open(file_path, "a") as file:
    file.write(user_input + "\n")
# makes room for the text to be added and recorded
print("""
<!-- Same form from previous assignment -->
<h1>In the form below, press 'enter' after inputting data</h1>
<h2>click 'Show Me' to see all previous data</h2>
<h2>click 'Deleat All' to delete all previous data</h2>
<!-- post data -->
<form method="post" action="cgi_script.py">
  <p>Enter your data: <input type="text" name="user_input"></p>
      <p>previously entered data: %s</p>
</form>

""" % user_input)
user_output: str = form.getvalue("user_output", "")

if "button" in form:
  with open(file_path,"r") as file:
      user_output = file.read() + '\n'
print("""  
<form method="post" action="cgi_script.py">
    <p>all previous data: %s</p>
    <input type="submit" name="button" value="Show Me">
  </form>
""" % user_output)

# form to delete all entries from the .txt memory file
if "deleat_button" in form:
  with open(file_path, "w") as file:
      file.write("")

# This next bit conatains the scripts needed for search, and for the two APIs
print(""" 
<br><br>  
<form method="post" action="cgi_script.py">
  <input type="submit" name="deleat_button" value="Deleat All">
</form>
      
<br><br>
<h1>Doge Energy RN!</h1>

<!-- fun song -->
<iframe src="https://www.youtube.com/embed/AhSEfKo0tlw" width="640" height="480" 
      frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe>

      
  <script>
    // DOMCOntentLoaded waits until the other contents of the page are loaded then the function
    document.addEventListener("DOMContentLoaded", function() {
        fetchNASAData();
    });

    // function to display the API photo and info
    function fetchNASAData() {
        // Keys are free for NASA API, if this key does not work, it is possible using 
        // `https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY` (be sure to use the backtick!)
        const apiKey = "ZrJCfy77fLoXejndMkgTthEacoyeqXFNffPn10dw";
        const apiUrl = `https://api.nasa.gov/planetary/apod?api_key=${apiKey}`;

        // This is the same form I used to get the Doge price
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                // Display data using a function
                displayData(data);
            })
            .catch(error => console.log(error));
    }


    // Function to actually display NASA API data to screen
    function displayData(data) {
        const imageElement = document.getElementById("NASA-image");
        const titleElement = document.getElementById("NASA-title");
        const explanationElement = document.getElementById("NASA-explanation");

        imageElement.src = data.url;
        titleElement.textContent = data.title;
        explanationElement.textContent = data.explanation;
    }

    document.getElementById("search_form").addEventListener("submit", function(event) {
      event.preventDefault();
      
      // lol I had a long time put into this part because of a Shakespearean typo "toLoerCase" is what I typed, omg
      // so much time went into this one silly mistake. But now it works!
    //   takes the input, trims whitespace and makes it all lowercase for parsing
      var searchQuery = document.getElementById("search_field").value.trim().toLowerCase();
      var pages = {
        // Very limited search options
        "sitemap":"../dir/sitemap.html", 
        "dogegraph": "../dir/dogegraph.html",
        "map":"../dir/sitemap.html", 
        "graph": "../dir/dogegraph.html",
        "help" : "../dir/help.html"
      };

    // this checks the "pages" var for the searchquery, if it is present,
    // go to that page
      if (pages.hasOwnProperty(searchQuery)) {
        window.location.href = pages[searchQuery];
      }
      else {
        alert("Page Not Found!");
      }
    });

    // Function to fetch and update the DOGE price
    function fetchDogePrice() {
      const apiUrl = `https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd`;

      // Fetch DOGE price from CoinGecko API I think it updates every 10 mins
      fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
          const dogePrice = data.dogecoin.usd;
          console.log('updoot the prooce, ', dogePrice);
          document.getElementById('doge_price').innerText = `$${dogePrice} USD`;
        })
        .catch(error => {
          console.error('Error fetching DOGE price:', error);
          document.getElementById('doge_price').innerText = 'Only 5 price fetches per minute';
        });
    }

    fetchDogePrice();
    setInterval(fetchDogePrice, 30000);

  </script>
</body>
</html>
""")