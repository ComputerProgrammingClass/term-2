import requests


def display_fun_cat_facts(data):
    print("HERE ARE SOME FUN CAT FACTS !!!")
    facts = data["data"]

    for fact in facts:
        print(f"FUN FACT: {fact}")


res = requests.get("https://meowfacts.herokuapp.com", params={"count": 3})

display_fun_cat_facts(res.json())
