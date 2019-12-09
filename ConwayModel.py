import numpy as np
import pygame


class ConwayModel:
    def __init__(self, width, height, wrapping=True):
        self.width = width
        self.height = height
        self.wrapping = wrapping
        self.grid = np.zeros((width, height))
        self.visual_grid = np.ones((width, height, 3))
        self.surface = pygame.surfarray.make_surface(255 * np.reshape(self.grid, (width, height, 1)) * self.visual_grid)

    def next(self):
        total: np.ndarray = np.zeros((self.width, self.height))
        total[:-1, :] += self.grid[1:, :]
        total[1:, :] += self.grid[:-1, :]

        total[:, :-1] += self.grid[:, 1:]
        total[:, 1:] += self.grid[:, :-1]

        total[1:, :-1] += self.grid[:-1, 1:]
        total[1:, 1:] += self.grid[:-1, :-1]

        total[:-1, :-1] += self.grid[1:, 1:]
        total[:-1, 1:] += self.grid[1:, :-1]

        if self.wrapping:
            total[-1:, 1:] += self.grid[:1, :-1]
            total[:1, 1:] += self.grid[-1:, :-1]

            total[1:, -1:] += self.grid[:-1, :1]
            total[1:, :1] += self.grid[:-1, -1:]

            total[-1:, :-1] += self.grid[:1, 1:]
            total[:1, :-1] += self.grid[-1:, 1:]

            total[:-1, -1:] += self.grid[1:, :1]
            total[:-1, :1] += self.grid[1:, -1:]

            total[-1:, :] += self.grid[:1, :]
            total[:1, :] += self.grid[-1:, :]

            total[:, -1:] += self.grid[:, :1]
            total[:, :1] += self.grid[:, -1:]

            total[:1, -1:] += self.grid[-1:, :1]
            total[:1, :1] += self.grid[-1:, -1:]

            total[-1:, -1:] += self.grid[:1, :1]
            total[-1:, :1] += self.grid[:1, -1:]

        self.grid = ((4 > total) & (total > 1) & ((self.grid == 1) | (total == 3))).astype(int)

    def update_surface(self):
        self.surface = pygame.surfarray.make_surface(
            255 * np.reshape(self.grid, (self.width, self.height, 1)) * self.visual_grid)

    def draw_area(self, screen: pygame.Surface, x: int, y: int, width: int, height: int):
        self.update_surface()
        screen.blit(pygame.transform.scale(self.surface, (width, height)), (x, y))

    def draw_resolution(self, screen: pygame.Surface, x: int, y: int, square_size: int):
        self.update_surface()
        screen.blit(pygame.transform.scale(self.surface, (self.width * square_size, self.height * square_size)), (x, y))

    def activate_pixel(self, x, y):
        self.grid[x, y] = 1

    def toggle_pixel(self, x, y):
        self.grid[x, y] = 0 if self.grid[x, y] == 1 else 0

    def deactivate_pixel(self, x, y):
        self.grid[x, y] = 0


if __name__ == '__main__':
    pixels = [501, 501]
    size = 2

    model = ConwayModel(pixels[0], pixels[1])

    grid = np.random.randint(0, 2, (pixels[0] , pixels[1]))
    # grid = np.ones((int(pixels[0] / 1.5), pixels[1] // 500))
    print(grid.shape)

    width_middle = (model.width // 2)
    height_middle = (model.height // 2)
    print(width_middle)
    print(height_middle)

    width_start = width_middle - ((len(grid) // 2))
    height_start = height_middle - ((len(grid[0]) // 2))
    print(width_start)
    print(height_start)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                model.activate_pixel(height_start + j, width_start + i)

    pygame.init()
    screen = pygame.display.set_mode([pixels[0] * size, pixels[1] * size])
    pygame.key.set_repeat(200, 10)

    running = True
    while running:
        model.draw_resolution(screen, 0, 0, size)
        model.next()
        pygame.display.flip()
        # pygame.time.delay(100)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
