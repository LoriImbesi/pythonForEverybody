import json
# This is a list of 2 dictionaries
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)     # "loads" pronounced load s -> means load string
print('Name:', info["name"])  # info is a dict
print('Hide:', info["email"]["hide"])
