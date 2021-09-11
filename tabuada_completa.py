#Author: https://github.com/charlyBraga
print("\n+++ Todas Tabuadas +++\n")
for tab in range(1,9+1):
    print(f"\n----------------\nTabuada de {tab}:")
    i=1
    while(i<=9):
        print(f"{tab} x {i} = {tab*i}")
        i+=1
