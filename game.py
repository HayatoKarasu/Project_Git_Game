import pygame
from random import shuffle

pygame.init()
pygame.display.set_caption('Игра на проверку зрительной памяти')
window_surface = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#FF00FF'))

button_font = pygame.font.SysFont('Verdana', 15) # используем шрифт Verdana
button_text_color = pygame.Color("black")
button_color = pygame.Color("gray")
button_rect = pygame.Rect(200, 250, 400, 100)
button_text = button_font.render('Нажми чтобы начать игру!', True, button_text_color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                # определяем цвета игры
                black = (0, 0, 0)
                white = (255, 255, 255)
                red = (255, 0, 0)
                blue = (0, 0, 255)
                green = (0, 255, 0)
                yellow = (255, 255, 0)
                purple = (128, 0, 128)
                grey = (192, 192, 192)

                screen_width = 800
                screen_height = 600
                screen = pygame.display.set_mode((screen_width, screen_height))
                pygame.display.set_caption("Тренируем визуальную память")

                # задаем параметры окружностей и перемешиваем пары
                circle_radius = 50
                circle_colors = [red, blue, green, yellow, purple, white]
                circle_pairs = circle_colors * 2
                shuffle(circle_pairs)

                # формируем список окружностей
                circle_positions = []
                for i in range(6):
                    for j in range(2):
                        center_x = ((screen_width / 6) * (i + 1)) - (screen_width / 12)
                        center_y = ((screen_height / 3) * (j + 1)) - (screen_height / 6)
                        circle_positions.append([center_x, center_y])

                # запоминаем позиции и цвета окружностей
                original_circle_positions = circle_positions.copy()
                original_circle_colors = circle_pairs.copy()

                # рисуем цветные окружности
                for i in range(len(circle_pairs)):
                    position = circle_positions[i]
                    color = circle_pairs[i]
                    pygame.draw.circle(screen, color, position, circle_radius)

                font = pygame.font.SysFont('Arial', 20)
                pygame.display.update()

                # ждем 5 секунд
                pygame.time.wait(5000)

                # закрываем цветные окружности серыми
                for i in range(len(circle_pairs)):
                    position = circle_positions[i]
                    pygame.draw.circle(screen, grey, position, circle_radius)

                pygame.display.update()
                uncovered_circles = []
                last_uncovered_circle = None
                score = 0

                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = event.pos
                            for i in range(len(circle_positions)):
                                position = circle_positions[i]
                                if ((position[0] - mouse_pos[0]) ** 2 + (position[1] - mouse_pos[1]) ** 2) ** 0.5 < circle_radius:
                                    if i not in uncovered_circles:
                                        uncovered_circles.append(i)
                                        color = original_circle_colors[i]
                                        pygame.draw.circle(screen, color, position, circle_radius)
                                        pygame.display.update()
                                        if last_uncovered_circle is not None and original_circle_colors[last_uncovered_circle] == original_circle_colors[i]:
                                            score += 1
                                        last_uncovered_circle = i

                            if len(uncovered_circles) == len(circle_pairs):
                                # вывод результата
                                final_score_text = font.render(f"Уровень памяти: {str(score)} из 6", True, white)
                                screen.blit(final_score_text, (screen_width // 2, screen_height // 2 + 125))
                                pygame.display.update()
                                pygame.time.wait(3000)
                                pygame.quit()
                                exit()

        window_surface.blit(background, (0, 0))
        pygame.draw.rect(window_surface, button_color, button_rect)
        button_rect_center = button_text.get_rect(center=button_rect.center)
        window_surface.blit(button_text, button_rect_center)
        pygame.display.update()

