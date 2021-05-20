magic = {

}


magig_file = open('magig.txt','r')
magig_file1 = magig_file.readlines()

for cur_magic in magig_file1:
    c= cur_magic.strip()
    pr = c.split(',')
    magic[pr[0]] = float(pr[1])

print(magic['Водопад'])