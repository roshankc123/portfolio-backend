import requests

headers = {"Authorization":"Bearer your_auth","Accept": "application/vnd.github+json"}
r = requests.get('https://api.github.com/users/your_username/repos?type=owner&sort=created', headers=headers)

# print(r.json())

final_count = {}

mySkills = ['Python', 'C++', 'JavaScript', 'HTML', 'CSS', 'PHP', 'Shell', 'C']

for i in r.json():
    # print(i['name'])
    temp_r = requests.get('https://api.github.com/repos/your_username/' + i['name'] + '/languages', headers=headers)
    # print(temp_r.json())
    lang = temp_r.json()
    # print(lang)
    for each_lang in lang.keys():
        if mySkills.count(each_lang) != 0:
            final_count[each_lang] = lang[each_lang] + 0 if final_count.get(each_lang) == None else final_count.get(each_lang)

# print(final_count)
# final_count.pop('Jupyter Notebook')
values = list(final_count.values())
total = sum(values)
for each_lang in final_count.keys():
    final_count[each_lang] /= total
    final_count[each_lang] = round(final_count[each_lang] * 100, 2)

print(final_count)