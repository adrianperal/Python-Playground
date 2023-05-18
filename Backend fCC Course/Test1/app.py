def readFile():
    file = open('./Backend fCC Course/Test1/sample.txt','r')
    for x in file.readlines():
        print(x)
    file.close()

def saveToFile(item):
    file = open('./Backend fCC Course/Test1/sample.txt','a')
    file.writelines(item + '\n')
    file.close()

item = input('Add item: ')
saveToFile(item)

readFile()
