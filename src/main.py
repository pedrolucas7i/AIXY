import logging
import vision
import tank
import utils
import env

things_to_find=[]

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def autonomous_drive(thing, localization=None):
    global things_to_find
    
    if not things_to_find:
        decision = vision.decide()
    else:
        decision = vision.find(thing, localization)

    utils.drive(utils.movements[decision].get('direction'), utils.movements[decision].get('speed'))
    utils.calculatedWaitingTime(0.7)


if __name__ == "__main__":
    print(f"AIXY (V{env.AIXY_SOFTWARE_VERSION}) ALIVE!!!")