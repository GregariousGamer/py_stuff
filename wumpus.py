#!/bin/python3

# Game #1 from '24 Tested Ready-To-Run games in Basic' by Ken Tracton

def main():
    header()

# header_func  
# {{{
def header():
    messages('header')
# }}}
# map_gen  
# {{{
def map_gen():
    pass
# }}}
# trap_gen  
# {{{
def trap_gen():
    pass
# }}}
# messages  
# {{{
def messages(*msg):
    output = {
            'wumpus_near': "I smell a Wumpus",
            'bat_near': "I hear a Bat",
            'pit_near': "I feel a Draft",
            'pit_fall': "A pit! China, here I comeeeeeeee!!!!",
            'wumpus_eat': "Dummy, you lose! The Wumpii just love you!!!",
            'wumpus_bump': "Dummy, you bumped into a wumpus!",
            'wumpus_kill': "Aha! You got the Wumpus!",
            'header': " "*32 + "HUNT THE WUMPUS\n" + "-"*80,
            'game_end': "Okay hot shot, the Wumpii will get their revenge\nWumpii spirits will haunt you til' then!",
            'introduction': """
    Welcome to 'Hunt the Wumpus'! The Wumpus lives in a cave with 20 rooms. Each room
    has 3 tunnels leading into other rooms (look at a d20, or icosahedron to see how
    this works).
        Hazards
    Bottomless pits - there are two of these. Fall into one, and you will land in China
    
    Super Bats - 2 other rooms have these. If you go there, a bat grabs you and takes
    you to another room (which may be troublesome)

        Wumpus
    The Wumpus is not bothered by the hazards (he has sucker feet and and is
    too big for a bat to lift). Usually he is asleep. Two things wake him up;
    your entering his room or your shooting an arrow. If the Wumpus wakes,
    he moves (75% chance), or stays still (25% chance). After that, if he where
    you are, he eats you up and you lose.

        You
    Each turn, you move or shoot a crooked arrow.
    Moving: You can go through one room (thru one tunnel)
    Arrows: You have 5 arrows. You lose when you run out.
    Each arrow can go through 1 to 5 rooms. You aim by telling
    the computer the room/s you want the arrow to go to. If the arrow can't
    go that way (ie no tunnel) it moves at random to the next room.
    If the arrow hits the wumpus, you win.
    If the arrow hits you, you lose.

        Warnings
    When you are one room away from the wumpus or a hazard,
    the computer says:
    Wumpus - 'I smell a Wumpus'
    Bat - 'I hear a Bat'
    Pit - 'I feel a draft'
    """,
    }
    for item in msg:
        print(output[item])
# }}}





if __name__ == "__main__":
    main()
