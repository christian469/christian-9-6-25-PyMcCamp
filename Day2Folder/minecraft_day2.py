# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def on_chat():
    agent.teleport_to_player()
player.on_chat("tp", on_chat)


def turnleft():
    agent.turn(TurnDirection.LEFT)
    
def on_chat2():
    pass
player.on_chat("tl", turnleft)

def turnright():
    agent.turn(RIGHT)

player.on_chat("tr", turnright)

def moveUp():
    agent.move(UP, 1)

def on_chat3():
    pass
player.on_chat("fly", on_chat3)

def mvdown():
    agent.move(DOWN, 1)
    def on_chat4():
        pass
player.on_chat("down", mvdown)

def obby1():
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    pass
player.on_chat("obby1", obby1)

def obby2():
    agent.move(BACK, 1)

player.on_chat("BACK", obby2)