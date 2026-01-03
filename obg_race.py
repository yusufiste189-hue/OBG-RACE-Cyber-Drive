import pygame
import random
import sys

# OBGCyber - Analyze. Secure. Dominate.
# PROJECT: OBG-RACE (Cyber Drive)

# [TR] Başlatma | [EN] Initialization
pygame.init()

# [TR] Renkler | [EN] Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN  = (0, 255, 255) # Player Car
RED   = (255, 50, 50) # Enemy Car

# [TR] Ekran Ayarları | [EN] Screen Settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OBG-RACE: CYBER DRIVE")

clock = pygame.time.Clock()

def start_game():
    car_w, car_h = 50, 80
    x = (WIDTH // 2) - (car_w // 2)
    y = HEIGHT - 100
    speed = 8

    enemy_w, enemy_h = 50, 50
    enemy_x = random.randint(0, WIDTH - enemy_w)
    enemy_y = -100
    enemy_speed = 7

    score = 0
    font = pygame.font.SysFont("Arial", 25)

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x -= speed
        if keys[pygame.K_RIGHT] and x < WIDTH - car_w:
            x += speed

        enemy_y += enemy_speed

        if enemy_y > HEIGHT:
            enemy_y = -enemy_h
            enemy_x = random.randint(0, WIDTH - enemy_w)
            score += 1
            enemy_speed += 0.3 

        player_rect = pygame.Rect(x, y, car_w, car_h)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_w, enemy_h)

        if player_rect.colliderect(enemy_rect):
            # [TR] Konsol Çıktısı | [EN] Console Output
            print(f"\n[!] CRASH DETECTED / KAZA YAPILDI!")
            print(f"[!] FINAL SCORE / SKORUN: {score}")
            running = False

        pygame.draw.rect(screen, CYAN, player_rect)
        pygame.draw.rect(screen, WHITE, (WIDTH//2 - 2, 0, 4, HEIGHT), 1)
        pygame.draw.rect(screen, RED, enemy_rect)

        # [TR] Ekranda Skor | [EN] On-screen Score
        score_text = font.render(f"Score/Skor: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    start_game()