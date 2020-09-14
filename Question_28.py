temp='canioe 22536 for 445 solutions'
data=[x for x in (int(x)for x in temp if x.isdigit())if x%2==0]
print(data)
