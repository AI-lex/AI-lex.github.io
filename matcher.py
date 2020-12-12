import random
import json


# generate list
## table data structure: name / wish decr / token /

json_list = {
    "token1" :{
        "name": "Johanna",
        "match": "",
        "descr": "windelweich",
        "wish": "windel",
        "img": "/img/img1.png"
    },
    "token2" :{
        "name": "Hussein",
        "match": "",
        "descr": "windelweich",
        "wish": "ziggen",
        "img": "/img/img2.png"
    },
    "token3" :{
        "name": "Viola",
        "match": "",
        "descr": "windelweich",
        "wish": "koks",
        "img": "/img/img3.png"
    },
    "token4" :{
        "name": "Maxim",
        "match": "",
        "descr": "windelweich",
        "wish": "windelweich",
        "img": "/img/img4.png"
    },

    "token5" :{
        "name": "Alexander",
        "match": "",
        "descr": "windelweich",
        "wish": "windelweich",
        "img": "/img/img5.png"
    }
}

def pick_random(pool):

    index_random_pick = random.randint(0, (len(pool) -1))

    return pool[index_random_pick]


## match logic
match_pool = ["Johanna", "Hussein", "Viola", "Maxim", "Alexander"]
token_list = ["token1", "token2", "token3", "token4", "token5"]
random.shuffle(token_list)


for token in token_list:

    temp_list = match_pool[::-1]
    pname = json_list[token]["name"]

    # remove name in matching list
    if(pname in temp_list):
        temp_list.remove(pname)

    # random pick of name in list
    match_name = pick_random(temp_list)

    #drop matched name out of list
    match_pool.remove(match_name)

    #print(str(json_list[token]["name"]) + " hat gezogen: " + str(match_name))
    json_list[token]["match"] = match_name
# output list

try:
    with open('data.json', 'w') as f:
        json.dump(json_list, f)
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()