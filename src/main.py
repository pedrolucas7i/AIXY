import threading
import logging
import time
import pygame
import controller
import vision
import utils
import conversation
import brain
import tts
import env

# Initialize logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Global variable to switch between AI and manual mode
manual_mode = False

# Function to handle autonomous driving
def drive(thing, localization=None):
    while True:
        if manual_mode:
            controller.manualControl()
            continue  # Skip AI processing while in manual mode

        utils.verifyObstacules()

        if thing is None:
            decision = vision.decide().strip().strip("'").lower()
        else:
            decision = vision.find(thing, localization).strip().strip("'").lower()

        utils.drive(decision, utils.movements[decision].get('speed'))
        utils.calculatedWaitingTime(0.7)

# Function to handle conversation
def human_interaction():
    while True:
        conversation.commonConversations()

# Function to listen for Xbox controller input
def joystick_listener():
    global manual_mode
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        print("No controller connected.")
        return

    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Controller connected: {joystick.get_name()}")

    while True:
        pygame.event.pump()
        # Xbox button is usually button index 8
        xbox_button = joystick.get_button(8)

        if xbox_button:
            manual_mode = not manual_mode
            mode = "MANUAL" if manual_mode else "AUTONOMOUS"
            print(f"Switched to {mode} mode.")
            tts.speek(f"{mode} mode activated.")
            time.sleep(1.5)  # Prevent multiple toggles from one press

# Main execution
if __name__ == "__main__":
    print(f"AIXY (V{env.AIXY_SOFTWARE_VERSION}) ALIVE!!!")
    tts.speak(text)

    # Start AI driving thread
    ai_thread = threading.Thread(target=drive, args=(None, None), daemon=True)
    ai_thread.start()

    # Start human interaction thread
    convo_thread = threading.Thread(target=human_interaction)
    convo_thread.start()

    # Start obstacle detection thread
    obstacle_thread = threading.Thread(target=utils.verifyObstacules)
    obstacle_thread.start()

    # Start Xbox controller listener
    joystick_thread = threading.Thread(target=joystick_listener, daemon=True)
    joystick_thread.start()
