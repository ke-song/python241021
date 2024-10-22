import pygame
import random
import time

# 초기화
pygame.init()

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (255, 0, 0),    # 빨강
    (0, 255, 0),    # 초록
    (0, 0, 255),    # 파랑
    (255, 255, 0),  # 노랑
    (255, 0, 255),  # 마젠타
    (0, 255, 255),  # 시안
    (255, 128, 0)   # 주황
]

# 게임 설정
CELL_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * (GRID_WIDTH + 6)
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

# 테트로미노 모양 정의
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.randint(0, len(COLORS) - 1)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("테트리스")
        self.clock = pygame.time.Clock()
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = Tetromino()
        self.next_piece = Tetromino()
        self.game_over = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.font = pygame.font.Font(None, 36)
        self.last_fall_time = time.time()
        self.fall_speed = 0.5

    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x] is not None:
                    pygame.draw.rect(self.screen, COLORS[self.grid[y][x]], 
                                     (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(self.screen, WHITE, 
                                     (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    def draw_piece(self, piece, offset_x, offset_y):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, COLORS[piece.color], 
                                     ((piece.x + x + offset_x) * CELL_SIZE, 
                                      (piece.y + y + offset_y) * CELL_SIZE, 
                                      CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(self.screen, WHITE, 
                                     ((piece.x + x + offset_x) * CELL_SIZE, 
                                      (piece.y + y + offset_y) * CELL_SIZE, 
                                      CELL_SIZE, CELL_SIZE), 1)

    def draw_next_piece(self):
        for y, row in enumerate(self.next_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, COLORS[self.next_piece.color], 
                                     ((GRID_WIDTH + 1 + x) * CELL_SIZE, 
                                      (1 + y) * CELL_SIZE, 
                                      CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(self.screen, WHITE, 
                                     ((GRID_WIDTH + 1 + x) * CELL_SIZE, 
                                      (1 + y) * CELL_SIZE, 
                                      CELL_SIZE, CELL_SIZE), 1)

    def move(self, dx, dy):
        if not self.collision(dx, dy):
            self.current_piece.x += dx
            self.current_piece.y += dy
            return True
        return False

    def collision(self, dx, dy):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x, new_y = self.current_piece.x + x + dx, self.current_piece.y + y + dy
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or \
                            (new_y >= 0 and self.grid[new_y][new_x] is not None):
                        return True
        return False

    def lock_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece.y + y][self.current_piece.x + x] = self.current_piece.color
        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = Tetromino()
        if self.collision(0, 0):
            self.game_over = True

    def clear_lines(self):
        lines_cleared = 0
        for y in range(GRID_HEIGHT - 1, -1, -1):
            if all(cell is not None for cell in self.grid[y]):
                del self.grid[y]
                self.grid.insert(0, [None for _ in range(GRID_WIDTH)])
                lines_cleared += 1

        if lines_cleared > 0:
            self.score += lines_cleared ** 2 * 100 * self.level
            self.lines_cleared += lines_cleared
            self.level = self.lines_cleared // 10 + 1
            self.fall_speed = max(0.1, 0.5 - (self.level - 1) * 0.05)

    def rotate_piece(self):
        original_shape = self.current_piece.shape
        self.current_piece.rotate()
        if self.collision(0, 0):
            self.current_piece.shape = original_shape

    def run(self):
        while not self.game_over:
            current_time = time.time()
            delta_time = current_time - self.last_fall_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.move(1, 0)
                    elif event.key == pygame.K_DOWN:
                        self.move(0, 1)
                    elif event.key == pygame.K_UP:
                        self.rotate_piece()
                    elif event.key == pygame.K_SPACE:
                        while self.move(0, 1):
                            pass
                        self.lock_piece()

            if delta_time > self.fall_speed:
                if not self.move(0, 1):
                    self.lock_piece()
                self.last_fall_time = current_time

            self.screen.fill(BLACK)
            self.draw_grid()
            self.draw_piece(self.current_piece, 0, 0)
            self.draw_next_piece()

            score_text = self.font.render(f"점수: {self.score}", True, WHITE)
            level_text = self.font.render(f"레벨: {self.level}", True, WHITE)
            self.screen.blit(score_text, (GRID_WIDTH * CELL_SIZE + 10, CELL_SIZE * 6))
            self.screen.blit(level_text, (GRID_WIDTH * CELL_SIZE + 10, CELL_SIZE * 7))

            pygame.display.flip()
            self.clock.tick(60)

        game_over_text = self.font.render("게임 오버!", True, WHITE)
        final_score_text = self.font.render(f"최종 점수: {self.score}", True, WHITE)
        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2 - 30))
        self.screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 10))
        pygame.display.flip()
        pygame.time.wait(5000)

if __name__ == "__main__":
    game = Tetris()
    game.run()
    pygame.quit()