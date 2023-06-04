import requests
import json
import base64

# you can use api without authentication but there is limit, so use authentication if you want to extend your limits
headers = {} #{"Authorization":"Bearer your_auth_code","Accept": "application/vnd.github+json"}

def fetch_repos():

    r = requests.get('https://api.github.com/users/your_username/repos?type=owner&sort=created', headers=headers)
    # print(r.json())

    mySkills = ['Python', 'C++', 'JavaScript', 'HTML', 'CSS', 'PHP', 'Shell', 'C']

    data = {}
    count = 0

    for i in r.json():
        temp_r = requests.get('https://api.github.com/repos/your_username/' + i['name'] + '/languages', headers=headers)
        # print(temp_r.json())

        lang = temp_r.json()
        total = sum(list(lang.values()))    #total byte of code
        # # print(lang)

        lang_temp= {}

        for each_lang in lang.keys():
            if mySkills.count(each_lang) != 0:   #to filter the language that i have worked on myself
                lang_temp[each_lang] = round(lang[each_lang] / total * 100, 2)  #extract the percentage form byte
                # print(lang_temp)
        data.update({count : {'id' : count, 'name' : i['name'], 'url' : i['html_url'], 'description' : i['description'], 'time' : i['created_at'], 'update_at' : i['updated_at'], 'homepage': i['homepage'] , 'langs' : lang_temp}})
        count += 1
    
    return data
# fetch_repos()

def update_repos():
    fp = open(open('wd','r').read()+'/repos.json', 'w')
    fp.write(json.dumps(fetch_repos()))
    return

# update_repos()

def get_repos():
    fd = json.load(open(open('wd','r').read()+'/repos.json', 'r'))
    return dict(fd)

# send_repos()

# def fetch_readme(name):
#     r = requests.get('https://api.github.com/repos/your_user_name/'+ name +'/contents/README.md', headers=headers)
#     content = r.json()['content']
#     a = str(base64.b64decode(content))
#     return a.replace("\\n", "<br>")

# def update_readme(name):
#     fd = dict(json.load(open('readme.json', 'r+')))
#     # print(fd)
#     fd.update({name : fetch_readme(name)})
#     open('readme.json', 'w').write(json.dumps(fd))

# update_readme('AI_Web_Architecture')