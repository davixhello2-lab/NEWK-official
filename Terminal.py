import os

""

@staticmethod
def ttprintt(text):
    print(text)

def ppcolor(color):
    os.system(f"color {color}")

while True:
    player = input(">? ")

    if player.startswith("ttprintt "):
        texd = player[len("ttprintt "):]
        ttprintt(texd)

    elif player.startswith("ppcolor "):
          cor = player[len("ppcolor "):]
          ppcolor(cor)
