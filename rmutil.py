import os
class util:
    def __init__(self):
        return
    def do(self):
        remove = ["ai","computers","health","history","literature","psychology","science"]
        c = 0
        m = len(remove)
        base = "/home/matt/.local/lib/python3.6/site-packages/chatterbot_corpus/data/english/"
        while c != m:
            this = str(remove[c])
            tp = base + this + ".yml"
            if os.path.exists(tp):
                os.system("sudo rm " + tp)
            c += 1

        if os.path.exists(base + "cosby.yml"):
            os.system("sudo rm " + base + "cosby.yml")
            os.system("sudo cp cosby.yml " + base + "cosby.yml")
