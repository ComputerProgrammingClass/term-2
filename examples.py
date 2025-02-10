import requests

url = "https://wttr.in/Richmond+BC"

# j1 to specify json response
res = requests.get(url, params={"format": "j1"})

# read the documentation or look at the json to figure this out
temperature_c = res.json()["current_condition"][0]["temp_C"]
print(f"It is {temperature_c} degrees celsius in richmond bc")
