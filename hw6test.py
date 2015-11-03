"""test hw 06"""
def my_read_file_v2(fnm):
    """REad and print every line of the file.
    Removed teh \n at the end of the strings"""
    fp = open(fnm, 'r')
    t1=[]

    for line in fp:
        line = line.strip()
        t1.append(line)# remove \n, reassign
    print(t1)
    i=0
    print(t1[0])
    fp.close()

def main():
   
    table=my_read_file_v2('data1_gpa.txt')

main()
