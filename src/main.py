import threading
import logging
import vision
import utils
import conversation
import brain
import tts
import env


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def autonomous_drive(thing, localization=None):
    while True:
        if not thing:
            decision = next(vision.decide())
        else:
            decision = next(vision.find(thing, localization))

        utils.drive(utils.movements[decision].get('direction'), utils.movements[decision].get('speed'))
        utils.calculatedWaitingTime(0.7)


def human_interaction():
    while True:
        conversation.commonConversations()


if __name__ == "__main__":
    print(f"AIXY (V{env.AIXY_SOFTWARE_VERSION}) ALIVE!!!")
    tts.text_to_speech(env.FIRST_EN_MESSAGE)
    LVMAD_processor = threading.Thread(target=autonomous_drive, args=(None, None), daemon=True)
    LVMAD_processor.start()
    LLMAC_processor = threading.Thread(target=human_interaction)
    LLMAC_processor.start()