
def main():
    places=[["123 Main","TX",76103],["456 Oak","AR",72201],["987 Rodeo","CA",90212],["1600 Pennslyvania","DC",20500]]
    size=len(places)
    i=0
    while i<size-1:
        if places[i][1]>places[i+1][1]:
            print(places[i][0])
        else:
            print(places[i][1])
        i+=1
    i=0
    while i<size-1:
        if (places[i][2]<75000) and (places[i+1]!=72201):
            print(places[i][2])
        else:
            print("No Match")
        i+=1
        

main()
