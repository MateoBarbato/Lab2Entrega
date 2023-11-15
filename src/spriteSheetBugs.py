
def loadSpritesBugs(sheet, spritSizeWidth, spritSizeHeight, rows, cols):
    rows = rows
    cols = cols

    dictKeys = ['down', 'rigth', 'left']
    spriteRow = dict()
    for row in range(rows):
        currentKey = dictKeys[row]
        spriteRow[currentKey] = []
        for i in range(cols):
            spriteRow[currentKey].append(sheet.subsurface(
                spritSizeWidth * i, spritSizeHeight * row, spritSizeWidth, spritSizeHeight))
    # print(spriteRow)
    return spriteRow
