def load(fnm):
    fp=open(fnm)
    d={}
    for f_line in fp:
        S=f_line.strip() # remove.\n
        L=S.split(',') # L =['NY','US']
        city=L[0]
        country=L[1]
        if country in d: # update the list
            d[country].append(city) #['NY','LA].append('boston')
        else:
            d[country]=[city] #eg 'RO':['bucharest']
    return d

def print_d(d):
    S_key=sorted(d)
    for country in d:
        print(country, ":", len(d[country]))
        print(d[country])

def main():
    d=load('cities.txt')
    print_d(d)

main()
    
