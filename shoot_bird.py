import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shoot the Bird")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Load Background Image from local file
background = pygame.image.load("./image/forest.jpg")  # Use the local image file

# Bird Class
class Bird:
    def __init__(self):
        self.x = random.randint(50, SCREEN_WIDTH - 50)
        self.y = random.randint(50, SCREEN_HEIGHT - 50)
        self.size = 40  # You can adjust the size as needed
        self.speed = 5
        
        # Load the bird image (make sure the image file exists in the directory)
        self.image = pygame.image.load("./image/bird.png")  # Bird image file

        # Resize the image to fit the bird's size
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        # Random velocity for the bird (smooth movement)
        self.vel_x = random.choice([-self.speed, self.speed])
        self.vel_y = random.choice([-self.speed, self.speed])

    def move(self):
        # Move the bird based on its velocity
        self.x += self.vel_x
        self.y += self.vel_y

        # Keep the bird within the screen bounds
        if self.x < 0: 
            self.x = 0
            self.vel_x *= -1  # Reverse direction when hitting the left boundary
        if self.x > SCREEN_WIDTH - self.size: 
            self.x = SCREEN_WIDTH - self.size
            self.vel_x *= -1  # Reverse direction when hitting the right boundary
        if self.y < 0: 
            self.y = 0
            self.vel_y *= -1  # Reverse direction when hitting the top boundary
        if self.y > SCREEN_HEIGHT - self.size: 
            self.y = SCREEN_HEIGHT - self.size
            self.vel_y *= -1  # Reverse direction when hitting the bottom boundary

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# Draw scope
def draw_scope(x, y):
    pygame.draw.circle(screen, RED, (x, y), 20, 2)  # Outer circle
    pygame.draw.circle(screen, BLACK, (x, y), 10, 2)  # Inner circle
    pygame.draw.line(screen, BLACK, (x - 25, y), (x + 25, y), 2)  # Horizontal line
    pygame.draw.line(screen, BLACK, (x, y - 25), (x, y + 25), 2)  # Vertical line

# Menu Functions
def draw_text(text, font, color, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    screen.blit(textobj, textrect)

def main_menu():
    font = pygame.font.SysFont(None, 50)
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)
        draw_text("Main Menu", font, BLACK, SCREEN_WIDTH // 2, 100)
        draw_text("Play", font, BLACK, SCREEN_WIDTH // 2, 200)
        draw_text("Settings", font, BLACK, SCREEN_WIDTH // 2, 300)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw_scope(mouse_x, mouse_y)  # Draw scope around the mouse pointer

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 200 < mouse_x < 600 and 180 < mouse_y < 220:
                    game()  # Start the game
                elif 200 < mouse_x < 600 and 280 < mouse_y < 320:
                    settings()  # Open settings menu

        pygame.display.flip()
        clock.tick(30)

# Game Function
def game():
    clock = pygame.time.Clock()
    birds = [Bird() for _ in range(5)]  # Create 5 birds
    score = 0

    while True:
        screen.blit(background, (0, 0))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw_scope(mouse_x, mouse_y)  # Draw scope around the mouse pointer

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for bird in birds:
                    if bird.x < mouse_x < bird.x + bird.size and bird.y < mouse_y < bird.y + bird.size:
                        birds.remove(bird)
                        birds.append(Bird())
                        score += 1
                        print(f"Score: {score}")

        for bird in birds:
            bird.move()
            bird.draw()

        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

# Settings Menu Function
def settings():
    font = pygame.font.SysFont(None, 50)
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)
        draw_text("Settings", font, BLACK, SCREEN_WIDTH // 2, 100)
        draw_text("Back", font, BLACK, SCREEN_WIDTH // 2, 200)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw_scope(mouse_x, mouse_y)  # Draw scope around the mouse pointer

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 200 < mouse_x < 600 and 180 < mouse_y < 220:
                    main_menu()

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main_menu()
