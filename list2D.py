list1=[]
list2 = [[]]
list2 = [
["Andi", "Budi"], 
["Cici", "Dedi"]]

def show(list):
    for i in range(len(list2)):
        for j in range(len(list2[i])):
            print(list2[i][j])

print(list2)