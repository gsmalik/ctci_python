import numpy as np


def paint_fill(new_color, screen_loc_row, screen_loc_col):
    """
    Function to change color in matching color masks.

    Parameters
    ----------
    new_color: str
        The new color to fill in.
    screen_loc_row: int
        The row coordinate of the pixel from which paint filling needs to start.
    screen_loc_col: int
        The column coordinate of the pixel from which paint filling needs to start.

    Time Complexity
    ---------------
    O(N), where N is the number of pixels on the screen. In the worst case, you might
    have to update all pixels on the screen.

    Space Complexity
    ----------------
    O(N), where N is the number of pixels on the screen. You create a screen sized
    'updated' np array to keep a track of which pixels have been updated. Also, in
    the worst case, the recursion stack can be N deep.
    """
    # probe original color
    screen_loc_color = screen[screen_loc_row][screen_loc_col]
    # update to new color
    screen[screen_loc_row][screen_loc_col] = new_color
    # mark this pixel as updated
    updated[screen_loc_row][screen_loc_col] = 1
    # iterate through neighbor pixels
    for row_cord_rel in [-1, 0, 1]:
        for col_cord_rel in [-1, 0, 1]:
            # check validity of neighbor pixel coordinates
            if (
                0 <= screen_loc_row + row_cord_rel < screen.shape[0]
                and 0 <= screen_loc_col + col_cord_rel < screen.shape[1]
            ):
                new_row_cord = screen_loc_row + row_cord_rel
                new_col_cord = screen_loc_col + col_cord_rel
                # if color matches and the neighbor pixel has not been updated before,
                # then call the paint fill function on this pixel.
                if (
                    screen[new_row_cord][new_col_cord] == screen_loc_color
                    and updated[new_row_cord][new_col_cord] == 0
                ):
                    paint_fill(
                        new_color=new_color,
                        screen_loc_row=new_row_cord,
                        screen_loc_col=new_col_cord,
                    )


n = 5
# create a global mutable np 2darray for the screen
screen = np.random.choice(["R", "G", "B"], size=(n, n))
# create a global mutable np 2darray to keep a track of which pixels have been
# updated
updated = np.zeros((n, n))

print(screen)
pixel_r = 1
pixel_c = 1
paint_fill("B", pixel_r, pixel_c)
print(screen)