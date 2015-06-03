# Returns a tuple of coords that represent,
# in order, width, height, xPos, yPos of a window.
def get_window_geometry(window):
    l = []
    curr_value = ""
    
    for letter in window.geometry():
        if letter.isdigit():
            curr_value += letter
        else:
            l.append(curr_value)
            curr_value = ""
    l.append(curr_value)
    
    return tuple(map(int, l))
