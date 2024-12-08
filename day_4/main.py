
def part1():
    file = open("input.txt", "r")
    word_search = file.read().split("\n")
    row, col = len(word_search), len(word_search[0])
    total_count = 0
    #print(row, col)
    target = 'XMAS'
    directions = [
        (0,1),
        (0,-1),
        (1,0),
        (-1,0),
        (1,1),
        (-1,-1),
        (1,-1),
        (-1,1)
    ]
    
    def is_valid(x, y, dx, dy):
        for i in range(len(target)):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < row and 0 <= ny < col) or word_search[nx][ny] != target[i]:
                return False
        return True

    
    for r in range(row):
        for c in range(col):
            for dx, dy in directions:
                if is_valid(r, c, dx, dy):
                    total_count += 1
    return total_count

print(part1())