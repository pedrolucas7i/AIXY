import pygame
import tank
import utils

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("Nenhum joystick encontrado.")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Conectado ao: {joystick.get_name()}")

try:
    while True:
        pygame.event.pump()
        
        eixo_y = joystick.get_axis(1)  # Eixo Y do analógico esquerdo
        eixo_x = joystick.get_axis(0)  # Eixo X do analógico esquerdo
        
        if abs(eixo_y) > 0.1:
            velocidade = int((1 - abs(eixo_y)) * 100)
            if eixo_y < 0:
                utils.drive('forward', 1)
            else:
                utils.drive('backward', 1)

        if abs(eixo_x) > 0.1:
            if eixo_x > 0:
                utils.drive('right', 2)
                
            else:
                utils.drive('left', 2)
        

        for i in range(joystick.get_numaxes()):
            axis_val = joystick.get_axis(i)
            if abs(axis_val) > 0.2:
                print(f"Eixo {i}: {axis_val:.2f}")

except KeyboardInterrupt:
    print("\nEncerrando...")
