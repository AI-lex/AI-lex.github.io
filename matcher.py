import random
import json


# generate list
## table data structure: name / wish decr / token /

json_list = {
    "diecachhh" :{
        "name": "Johanna",
        "match": "",
        "wish": "",
        "img": ""
    },
    "legsnoob" :{
        "name": "Hussein",
        "match": "",
        "wish": "",
        "img": ""
    },
    "swollak" :{
        "name": "Viola",
        "match": "",
        "wish": "",
        "img": ""
    },
    "machhini" :{
        "name": "Maxim",
        "match": "",
        "wish": "",
        "img": ""
    },

    "nono" :{
        "name": "Alexander",
        "match": "",
        "wish": "",
        "img": ""
    }
}

def pick_random(pool):

    index_random_pick = random.randint(0, (len(pool) -1))

    return pool[index_random_pick]


## match logic
match_pool = ["Johanna", "Hussein", "Viola", "Maxim", "Alexander"]
token_list = ["diecachhh", "legsnoob", "swollak", "machhini", "nono"]
wish_dict = {"Johanna": "Glossybox geht einfach immer",
             "Hussein": "Mach dir keinen Kopf. Ziggen von Camel oder Knoppas",
             "Viola": "Montenegranisch fuer Dummies",
             "Maxim": "Online Coaching Peter Zwegat",
             "Alexander": "Bartoel!! Dringend!!"}
img_dict = {"Johanna": "img/jo.JPG",
             "Hussein": "img/hu.JPG",
             "Viola": "img/vi.JPG",
             "Maxim": "img/ma.JPG",
             "Alexander": "img/al.JPG"}

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
    json_list[token]["wish"] = wish_dict[match_name]
    json_list[token]["img"] = img_dict[match_name]
# output list

try:
    with open('data.json', 'w') as f:
        json.dump(json_list, f)
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()