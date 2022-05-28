#H*****W****
#*E*** *O***
#**L*O***R*D
#***L*****L
# result = [H, E, ]
def convert1(s, numRows):
        result = [""] * numRows
        print(result)
        rowNumber = 0
        direction = 1       
        for i in range(len(s)):  #looping through each element
            result[rowNumber] = result[rowNumber] + s[i]
            if rowNumber < numRows -1 and direction == 1:
                rowNumber += 1
            elif rowNumber > 0 and direction == -1:
                rowNumber -= 1
            else:
                direction *= -1
                rowNumber += direction
        return ''.join(result)

if __name__ == "__main__":
    print(convert1("Hello World", 4))
    

