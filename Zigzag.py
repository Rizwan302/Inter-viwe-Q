def convert( s:str, numRows: int):
    if numRows == 1:
        return
    res = ""
    for r in range(numRows): # 0 to 3
        increment = 2 * (numRows - 1) # 2*3=6
        for i in range(r, len(s), increment): # r=0 # r=1, #r=2, 
            res += s[i] # (0-H, 6-W), (1-E,5-_ ,7-0)
            if (r > 0 and r < numRows -1 and i+increment - 2 * r < len(s)):
                # 0+6-2*0=6-----
                # 6+6-2*0=12----
                # 1+6-2*1=5
                res += s[i + increment - 2 * r]    
    return res
 # HWE OLORDLL
if __name__=="__main__":
    print(convert('HELLO WORLD',4))
    # print(convert("Programming", 4))

