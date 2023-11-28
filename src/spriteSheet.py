
def loadSprites(sheet, spritSizeWidth, spritSizeHeight, rows, cols, keys):
    """
    Loads and processes sprites from a sprite sheet.

    Args:
        sheet (pygame.Surface): The sprite sheet image.
        spritSizeWidth (int): The width of a single sprite.
        spritSizeHeight (int): The height of a single sprite.
        rows (int): The number of rows of sprites in the sprite sheet.
        cols (int): The number of columns of sprites in the sprite sheet.
        keys (list): A list of keys representing the different sprite animations.

    Returns:
        dict: A dictionary containing the sprite animations for each key.
    """
    rows = rows
    cols = cols

    dictKeys = keys
    spriteRow = dict()
    for row in range(rows):
        currentKey = dictKeys[row]
        spriteRow[currentKey] = []
        for i in range(cols):
            spriteRow[currentKey].append(sheet.subsurface(
                spritSizeWidth * i, spritSizeHeight * row, spritSizeWidth, spritSizeHeight))
    return spriteRow
