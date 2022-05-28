def convert(s, numRows):
    if numRows == 1:
        return
    row_map={row:"" for row in range(1, numRows+1)}
    row = 1
    up = True
    
    for letter in s:
        row_map[row] += letter
        if (row == 1) or ((row < numRows) and up):
            row += 1
            up = True
        else:
            row -= 1
            up = False
    converted = ""
    for row in range(1, numRows+1):
        converted += row_map[row]
    return converted

if __name__=="__main__":
    print(convert("Hello wold", 4))    