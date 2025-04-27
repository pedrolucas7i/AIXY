import utils
import tank
import tts
import env
import time

def executeCommand(stt_data):
    Motors = tank.Motor()
    clamp = tank.Clamp()

    commands_actions = [
        (env.COMMANDS[0], lambda: (tts.speak(f"{utils.getDistance()}{env.RESPONSES[0]}"))),
        (env.COMMANDS[1], lambda: (tts.speak(env.RESPONSES[1]), Motors.driveForward(2))),
        (env.COMMANDS[2], lambda: (tts.speak(env.RESPONSES[2]), Motors.driveLeft(3))),
        (env.COMMANDS[3], lambda: (tts.speak(env.RESPONSES[3]), Motors.driveRight(3))),
        (env.COMMANDS[4], lambda: (tts.speak(env.RESPONSES[4]), Motors.driveBackward(3))),
        (env.COMMANDS[5], lambda: (tts.speak(env.RESPONSES[5]), clamp.up())),
        (env.COMMANDS[6], lambda: (tts.speak(env.RESPONSES[6]), Motors.stop(), time.sleep(40), tts.speak("I'm back"))),
    ]

    for command, action in commands_actions:
        if command in stt_data:
            action()
            break