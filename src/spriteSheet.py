
def loadSprites(sheet, spritSizeWidth, spritSizeHeight, rows, cols, keys):
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
