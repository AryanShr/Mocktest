def convertTexttoJson(txt):
    sep = txt.replace("\n","").split(" ")
    ans = {}
    for i in range(0,len(sep)-1,2):
        key = sep[i][:-1]
        val = sep[i+1]
        ans[key] = val
    return ans


text = """1) 1 2) 4 3) 2 4) 2 5) 2 
6) 4 7) 4 8) 1 9) 1 10) 4 
11) 1 12) 4 13) 2 14) 2 15) 3 
16) 3 17) 2 18) 3 19) 4 20) 1 
21) 43 22) 3400 23) 150 24) 12 25) 20 
26) 9 27) 20 28) 2 29) 10 30) 5 """

# text = input()

ns = convertTexttoJson(text)
print(ns)