test = [0, 0, 0, 1, 2, 3, 4, 5, 6]  
test1 = [0, 0, 0, 1, 2, 3, 4, 5, 6]  

for _dummy in test:
    if(_dummy == 0):
        test.pop()
for item in test1:
    if(item == 0):
        test1.pop(0)

print(test)
print(test1)