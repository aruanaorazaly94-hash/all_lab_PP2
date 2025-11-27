import pygame
import time
import random
import psycopg2
import itertools

try:
    
    connection = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="12345", 
        host="127.0.0.1", 
        port="5432"
    )

    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")   

        print(f"Server version: {cursor.fetchone()}")

    name = str(input())
    point = 0
    i = 0

    with connection.cursor() as cursor:
        cursor.execute("SELECT user_name FROM snake")
        row = cursor.fetchall()
        rows = list(itertools.chain(*row))
        if name not in rows:
            cursor.execute(
                f"""INSERT INTO snake (user_name, user_score) VALUES
                ('{name}', '{point}');"""
            )
    # Цвета

    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(160, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 150, 200)
    yellow = pygame.Color(255, 255, 0)

    # Инициализация

    pygame.init()

    # Настройки

    window_x = 600
    window_y = 600

    snake_speed = 10

    pygame.display.set_caption('Snakes')
    game_window = pygame.display.set_mode((window_x, window_y))
    clock = pygame.time.Clock()
    FPS = 10

    pygame.display.set_icon(pygame.image.load("add_files/Snake_icon.png"))
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    snake_position = [105, 45]
    start_tick = pygame.time.get_ticks()

    # Тело змейки

    snake_body = [[105, 45],
                [90, 45],
                [75, 45],
                [60, 45]
                ]

    # Первое направление

    direction = 'RIGHT'
    change_to = direction

    # Счетчики

    score = 0
    global level
    level = 1
    count = 1
    timer = 0.1
    points = []
    for i in range(1, 81):
        points.append(i*50)

    # Табло


    def show_score(color, font, size):

        # Шрифт

        score_font = pygame.font.SysFont(font, size)
        level_font = pygame.font.SysFont(font, size)

        # Табло

        score_surface = score_font.render('Score : ' + str(score), True, color)
        level_surface = level_font.render('Level : ' + str(level), True, color)

        # Поверхностный объект

        score_rect = score_surface.get_rect()
        level_rect = level_surface.get_rect()

        # Отображение текста
        game_window.blit(score_surface, score_rect)
        game_window.blit(level_surface, (level_rect[0], level_rect[1] + 20))

    # Появление фруктов


    def spawn():
        position = [random.randrange(1, (window_x//15)) * 15,
                    random.randrange(1, (window_y//15)) * 15]
        return position

    # Синхрон поедания фруктов


    def check(position):
        test = True
        while test:
            count = 0
            for block in snake_body:
                if position[0] == block[0] and position[1] == block[1]:
                    position = spawn()
                count += 1
            if count == len(snake_body):
                test = False
        return position

    # Позиция фруктов


    fruit_position = [random.randrange(1, (window_x//15)) * 15,
                    random.randrange(1, (window_y//15)) * 15]
    fruit_spawn = True
    fruit_position = check(fruit_position)
    fruit_color = black

    # Функция "Game over"


    def game_over():

        # Шрифт

        my_font = pygame.font.SysFont('times new roman', 50)

        # Создание текстовой поверхности, на которой текст

        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, red)
        game_over_surface2 = my_font.render(
            'Your level is : ' + str(level), True, red)

        # Создание прямоугольного объекта для текста

        game_over_rect1 = game_over_surface.get_rect()
        game_over_rect2 = game_over_surface2.get_rect()

        # Установка положения текста

        game_over_rect1.midtop = (window_x/2, window_y/3.5)
        game_over_rect2.midtop = (window_x/2, window_y/4.7)

        # Отображение текста на экране

        game_window.blit(game_over_surface, game_over_rect1)
        game_window.blit(game_over_surface2, game_over_rect2)
        pygame.display.flip()

        # Выход

        time.sleep(2)
        quit()

    # Синхрон повышения уровня


    def level_up(score):
        global level
        kek = level
        count = 0
        for i in points:
            if i <= score:
                count += 1
        level = count+1
        if level > kek:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound("add_files/levelup.mp3"))

    # Основной цикл
    pause = True
    cnt = 0
    exit = True
    while exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False
            if event.type == pygame.USEREVENT:
                timer -= 0.00001

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                if event.key == pygame.K_SPACE:
                    if cnt % 2 == 0:
                            pause = False
                            cnt = cnt + 1
                    elif cnt % 2 == 1:
                            pause = True
                            cnt += 1


        # Если одновременно нажать две клавиши

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if pause == True:  
            
            # Перемещение змеи

            if direction == 'UP':
                snake_position[1] -= 15
            if direction == 'DOWN':
                snake_position[1] += 15
            if direction == 'LEFT':
                snake_position[0] -= 15
            if direction == 'RIGHT':
                snake_position[0] += 15

            # Механизм роста тела змеи

            snake_body.insert(0, list(snake_position))
            if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
                if fruit_color == green:
                    score += 70
                elif fruit_color == green:
                    score += 30
                elif fruit_color == red:
                    score += 10
                level_up(score)
                fruit_spawn = False
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("add_files/Eating.mp3"))
            else:
                snake_body.pop()

            
            
            with connection.cursor() as cursor:
                    cursor.execute(f"""DELETE FROM snake WHERE user_name = '{name}'""")

            with connection.cursor() as cursor:
                cursor.execute(
                    f"""INSERT INTO snake (user_name, user_score) VALUES
                    ('{name}', '{score}');"""
                )
                
                

            # Появление фруктов

            if not fruit_spawn:
                fruit_position = check(fruit_position)
                count += 1
                start_tick = pygame.time.get_ticks()

            fruit_spawn = True
            game_window.fill(black)

            # Таймер для фруктов

            if fruit_color == green:
                seconds = (tick-start_tick)/1000
                if seconds > 5.5:
                    fruit_position = check(spawn())
                    count += 1

            if fruit_color == green:
                seconds = (tick-start_tick)/1000
                if seconds > 4.5:
                    fruit_position = check(spawn())
                    count += 1
                    pygame.mixer.Channel(1).play(
                        pygame.mixer.Sound("add_files/Disappearing.mp3"))

            # Рисование частей змеи

            for pos in snake_body:
                pygame.draw.rect(game_window, blue,
                                pygame.Rect(pos[0], pos[1], 15, 15))

            if count % 10 == 0 and count > 0:
                pygame.draw.rect(game_window, green, pygame.Rect(
                    fruit_position[0], fruit_position[1], 15, 15))
                fruit_color = green
                tick = pygame.time.get_ticks()

            elif count % 5 == 0 and count > 0:
                pygame.draw.rect(game_window, green, pygame.Rect(
                    fruit_position[0], fruit_position[1], 15, 15))
                fruit_color = green
                tick = pygame.time.get_ticks()

            else:
                pygame.draw.rect(game_window, red, pygame.Rect(
                    fruit_position[0], fruit_position[1], 15, 15))
                fruit_color = red

            # Условия движения

            if snake_position[0] < 0:
                snake_position[0] += window_x+15
                direction = "LEFT"
            if snake_position[0] > window_x:
                snake_position[0] -= window_x+15
                direction = "RIGHT"
            if snake_position[1] < 0:
                snake_position[1] += window_y+15
                direction = "UP"
            if snake_position[1] > window_y:
                snake_position[1] -= window_y+15
                direction = "DOWN"

            # Касание к телу змеи

            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    pygame.mixer.Channel(5).play(pygame.mixer.Sound("add_files/death.mp3"))
                    game_over()

            # Непрерывное отображение счета

            show_score(white, 'times new roman', 20)
            pygame.display.update()
            clock.tick(FPS)
            
            with connection.cursor() as cursor:
                        cursor.execute(f"""DELETE FROM snake WHERE user_name = '{name}'""")

            with connection.cursor() as cursor:
                cursor.execute(
                    f"""INSERT INTO snake (user_name, user_score) VALUES
                    ('{name}', '{score}');"""
                )



except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")