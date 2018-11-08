import os
class util:
    def __init__(self):
        self.base = base = "~/.local/lib/python3.6/site-packages/chatterbot_corpus/data/english/"
        return
    def do(self):
        remove = ["ai","computers","health","history","literature","psychology","science"]
        c = 0
        m = len(remove)
        while c != m:
            this = str(remove[c])
            tp = self.base + this + ".yml"
            os.system("sudo rm " + tp)
            c += 1

        if os.path.exists(self.base + "cosby.yml"):
            os.system("sudo rm " + self.base + "cosby.yml")
            os.system("sudo cp cosby.yml " + self.base + "cosby.yml")


if __name__ == "__main__":
    r = util()
    r.do()
