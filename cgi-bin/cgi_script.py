#!python

# This file containing the html must be in a cgi-bin sub-directory.

import os
import cgi
import requests
import cgitb

print("content-type: text/html \n")

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
  <!-- add main page here -->

  <h1>Dogesplorer, the number one Doge explorer on the net!</h1>

    <nav class="main_nav">
      <!-- add nav links here -->
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

    <div class="price_display">
      <div id="doge_tag"><h3>Doge Price: </h3></div>
      <div id="doge_price">Finding latest price...</div>
    </div>



    <script>
      document.getElementById("search_form").addEventListener("submit", function(event) {
        event.preventDefault();
        
        // lol I had a long time put into this part because of a Shakespearean typo "toLoerCase" is what I typed, omg
        // I am sure you don't really care, but so much time went into this one silly mistake. But now it works!
        var searchQuery = document.getElementById("search_field").value.trim().toLowerCase();
        var pages = {
          "sitemap":"../dir/sitemap.html", 
          "dogegraph": "../dir/dogegraph.html",
          "map":"../dir/sitemap.html", 
          "graph": "../dir/dogegraph.html",
          "help" : "../dir/help.html"
        };

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
            // this is the part that gets the price from coingecko
            const dogePrice = data.dogecoin.usd;
            // writes to log. was using for debug
            console.log('updoot the prooce, ', dogePrice);
            // writes to page
            document.getElementById('doge_price').innerText = `$${dogePrice} USD`;
          })
          // I am not actually sure it's 5 calls per minute, but it's something like that.
          .catch(error => {
            console.error('Error fetching DOGE price:', error);
            document.getElementById('doge_price').innerText = 'Only 5 price fetches per minute';
          });
      }

      

      // Fetch DOGE price on page load
      fetchDogePrice();
      // this updates teh price every 30 seconds
      setInterval(fetchDogePrice, 30000);

    </script>

    <!-- these were all planned and forgotten. -->
    <!-- items: search bar, sitemap, graph, news video, news links -->
    <!-- articles: mini graph, current difficulty, number of blocks, recent trades -->
  
      <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
     
""")




# enable error handling (suggested by stackoverflow)
cgitb.enable(display=0,logdir="/var/www/cgi-bin/error-logs")

# declare file path
file_path = "user_message.txt"

# Get form data
form = cgi.FieldStorage()
user_input: str = form.getvalue("user_input", "")

# open in append mode because I wanted to get a list
with open(file_path, "a") as file:
    file.write(user_input + "\n")

# makes room for the text to be added and recorded
print("""
<h1>In the form below, press 'enter' after inputting data</h1>
<h2>click 'Show Me' to see all previous data</h2>
<h2>click 'Deleat All' to delete all previous data</h2>
<form method="post" action="cgi_script.py">
  <p>Enter your data: <input type="text" name="user_input"></p>
      <p>previously entered data: %s</p>
</form>
""" % user_input)

# declare new var for list display
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

print(""" 
<br><br>  
<form method="post" action="cgi_script.py">
  <input type="submit" name="deleat_button" value="Deleat All">
</form>
      
<br><br>
<h1>Doge Energy RN!</h1>

<iframe src="https://www.youtube.com/embed/AhSEfKo0tlw" width="640" height="480" 
      frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe>

</body>
</html>
""")