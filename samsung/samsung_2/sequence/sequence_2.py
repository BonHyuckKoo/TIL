a = list("Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.")
c = list("aeiou")

b = [x for x in a if x not in c]
    
print("".join(b))   
    

