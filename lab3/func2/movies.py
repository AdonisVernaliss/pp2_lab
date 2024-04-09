movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# print(movies[0]["name"])

def isAbove(d):
    if d["imdb"] > 5.5:
        return True
    else:
        return False

print (isAbove(movies[0]))


def listAbove():
    nl = []
    for i in movies:
        if isAbove(i):
            nl.append(i)
    return nl

print (listAbove())

def inCateg(st):
    nl = []
    for i in movies:
        if i["category"] == st:
            nl.append(i)
    return nl

print(inCateg("Romance"))


def aveImdb():
    s=0
    for i in movies:
        s+=i["imdb"]
    s/=len(movies)
    return s

print(aveImdb())

def aveCatImdb(st):
    s=0
    c=0
    for i in movies:
        if i["category"] == st:
            s+=i["imdb"]
            c+=1
    s/=c
    return s

print (aveCatImdb("Suspense"))
