# The Flask request object contains the data that the client (eg a browser) has sent to your app - ie the URL parameters, any POST data, etc.
# The requests library is for your app to make HTTP request to other sites, usually APIs. 
# It makes an outgoing request and returns the response from the external site
import requests
from .models import Quote

#You can get a random quote by requesting JSON feed for all random quotes
url = "http://quotes.stormconsultancy.co.uk/random.json"

def get_quote():
    """
    Function to consume http request and return a Quote class instance
    """
    response = requests.get(url).json()

    random_quote = Quote(response.get("author"), response.get("quote"))
    return random_quote