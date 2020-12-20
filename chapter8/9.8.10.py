import numpy as np


def fill_screen(color, color_neigh, pixel_r, pixel_c, screen, updated):
    if 0 <= pixel_c < np.shape(screen)[1] and 0 <= pixel_r < np.shape(screen)[0]:
        if updated[pixel_r][pixel_c] == 0 and (color_neigh == screen[pixel_r][pixel_c]):
            color_neigh = screen[pixel_r][pixel_c]
            updated[pixel_r][pixel_c] = 1
            screen[pixel_r][pixel_c] = color
            screen, updated = fill_screen(
                color, color_neigh, pixel_r, pixel_c - 1, screen, updated
            )
            screen, updated = fill_screen(
                color, color_neigh, pixel_r + 1, pixel_c - 1, screen, updated
            )
            screen, updated = fill_screen(
                color, color_neigh, pixel_r + 1, pixel_c, screen, updated
            )
            screen, updated = fill_screen(
                color, color_neigh, pixel_r + 1, pixel_c + 1, screen, updated
            )
            screen, updated = fill_screen(
                color, color_neigh, pixel_r, pixel_c + 1, screen, updated
            )
            screen, updated = fill_screen(
                color, color_neigh, pixel_r - 1, pixel_c + 1, screen, updated
            )
            screen, updated = fill_screen(
                color, color_neigh, pixel_r - 1, pixel_c, screen, updated
            )
            screen, updated = fill_screen(
                color, color_neigh, pixel_r - 1, pixel_c - 1, screen, updated
            )
            # updated[pixel_r][pixel_c] == 0
    return screen, updated


n = 5
screen = np.random.choice(["R", "G", "B"], size=(n, n))
updated = np.zeros((n, n))
print(screen)
pixel_r = 1
pixel_c = 1
fill_screen("B", screen[pixel_r][pixel_c], pixel_r, pixel_c, screen, updated)
print(screen)

