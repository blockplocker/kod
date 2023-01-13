import pygame
import pygame_gui

# Initialize Pygame
pygame.init()

pygame.display.set_caption("fight araz the game")
# Create a window
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#252525'))

manager = pygame_gui.UIManager((800, 600))


slider = pygame.Rect(100, 100, 200, 50)
slider_value = 0

araz_hp = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 600), (50, 25)), text='araz hp', manager=manager)

punch = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 400), (200, 80)), text='punch', manager=manager)

kick = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 400), (200, 80)), text="kick", manager=manager)



clock = pygame.time.Clock()
running = True

while running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user has clicked the mouse, update the value of the slider
            slider_value = event.pos[0]
            
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == punch:
                print("punch")
            elif event.ui_element == kick:
                print("kick")

        manager.process_events(event)
    pygame.draw.rect(window_surface, (255, 0, 0), slider)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
