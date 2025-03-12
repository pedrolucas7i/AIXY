import threading
import logging
import vision
import tank
import utils
import env


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def autonomous_drive(thing, localization=None):
    
    if not thing:
        decision = vision.decide()
    else:
        decision = vision.find(thing, localization)

    utils.drive(utils.movements[decision].get('direction'), utils.movements[decision].get('speed'))
    utils.calculatedWaitingTime(0.7)


if __name__ == "__main__":
    print(f"AIXY (V{env.AIXY_SOFTWARE_VERSION}) ALIVE!!!")
    LLMAD_processor = threading.Thread(target=autonomous_drive, args=(None, None), daemon=True)
    LLMAD_processor.start()