import vision
import utils

things_to_find=[]
movements = {
    "forward": {"direction": "forward", "speed": 2},
    "backward": {"direction": "backward", "speed": 2},
    "slow forward": {"direction": "forward", "speed": 1},
    "slow backward": {"direction": "backward", "speed": 1},
    "fast forward": {"direction": "forward", "speed": 3},
    "fast backward": {"direction": "backward", "speed": 3},
    "faster forward": {"direction": "forward", "speed": 4},
    "left": {"direction": "left", "speed": 2},
    "right": {"direction": "right", "speed": 2},
    "left fast": {"direction": "left", "speed": 3},
    "right fast": {"direction": "right", "speed": 3},
    "left very fast": {"direction": "left", "speed": 4},
    "right very fast": {"direction": "right", "speed": 4},
    "left hiper fast": {"direction": "left", "speed": 4},
    "right hiper fast": {"direction": "right", "speed": 4},
}


def autonomous_drive(thing, localization=None):
    global things_to_find
    
    if not things_to_find:
        decision = vision.decide()
        
    else:
        decision = vision.find(thing, localization)

    
        
    utils.calculatedWaitingTime(0.7)
    
result = movements["right fast"]
print(f"{result.get('direction')}\n{result.get('speed')}")