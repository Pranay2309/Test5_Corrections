D={1:{'A':{1:"A"},2:"B"},3:"C",'B':"D","D":'E'}
print(D[D[D[1][2]]],end="")
print(D[D["A"][2]])
# It will give key error
