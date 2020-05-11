import csv

def read_cell(x, y):
    with open('data/ctnlist.csv', 'r') as f:
        reader = csv.reader(f)
        y_count = 0 #flag variable
        for n in reader:
            if y_count == y:
                cell = n[x]
                return cell
            y_count += 1

#assigning values
j = 2
x = 0
y = 0
i = 2

ops_values = ('Add','Remove')
cell_null_values = (None, "")

with open('data/ctnlist.csv', 'r') as f:
    reader = csv.reader(f)
    total_columns = len(next(reader))
while(True):
    if i < total_columns:
        #print("outer loop" + str(i) + "," + str(j))
        soc_action = read_cell(i, j)# remove or delete (2,2) (3,3)(4,4)(5,5)
        if soc_action in ops_values: #condition check
            x = 0
            #if not null
            soc_name = read_cell(i, j+1)  # soc name that should be dynamic
            # that part needs to be dynamic
            file = open('{0}_{1}.csv'.format(soc_name, soc_action), "w")
            #use while loop and check upto null 5 times


            while(True):
                if y <= 5:
                    #print("inner loop" + str(i) + "," + str(j))
                    space = read_cell(i,j)  # (2,2) remove
                    #print(space)
                    if space in cell_null_values:  # check whether the cell is empty or not
                        y = y+1  # if empty then count empty cell as y
                        #print(y)
                    else:
                        file.write(str(read_cell(i,j)))  # if not empty call function write from (2,2)
                        file.write('\n')


                        y = 0
                    j = j+1
                else:
                    y = 0
                    break
        else:
            x = x+1
        j = 2
        i = i+1
    else:
        break

print("file has been successfully generated...")

