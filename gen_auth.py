import os

paths = ["consumer_key","consumer_secret","access_token","access_token_secret"]

c = 0
while c != len(paths):
    this = str(paths[c])
    if os.path.exists(this):
        os.remove(this)
    f = open(this,'w')
    f.write(input(this + "> "))
    c += 1
