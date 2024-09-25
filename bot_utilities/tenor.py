import requests
import json

# set the apikey and limit
apikey = "AIzaSyCYfdqxXqJfHRoiop_SBrjvkPkLXPRKYSE"   # click to set to your apikey
ckey = "my_test_app"  # set the client_key for the integration
lmt = 3
# our test search
search_term = "hatsune miku"

# get the top 8 GIFs for the search term
r = requests.get(
    "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))

if r.status_code == 200:
    # load the GIFs using the urls for the smaller GIF sizes
    top_8gifs = json.loads(r.content)
    print(top_8gifs)
else:
    top_8gifs = None
