def dynamicLineIntersection(n):
    #
    # Write your code here.
    #
    myMap = []
    for i in range(n):
        line = input()
        lineList = line.split()
        if len(lineList) == 3:
            lineList[0], lineList[1] = lineList[1], lineList[0]
        lineTrim = ''.join(lineList)
        #print(line, lineList, lineTrim)
        if lineList[1] == "+":
            # adding
            lineTrim = lineTrim.replace("+", "*")
            #print("adding to map", lineTrim)
            myMap.append(lineTrim)
            #print(myMap)
        elif lineList[1] == "-":
            # removing - guaranteed to be there
            lineTrim = lineTrim.replace("-", "*")
            #print("removing from map", lineTrim)
            myMap.remove(lineTrim)
            #print(myMap)
        elif lineList[0] == "?":
            # running query
            q = int(lineList[1])
            #print("q: ", q)
            counter = 0
            for eqn in myMap:
                #print(eqn)
                kb = eqn.replace("*", " ").split()
                # if y = kx + b
                k, b = int(kb[0]), int(kb[1])
                x = (q - b) / k
                print("x is: ", x)
                if x.is_integer():
                    counter += 1
            #print("counter: ", counter)
            print(counter)
                

if __name__ == '__main__':
    n = int(input())

    dynamicLineIntersection(n)


'''
4
+ 1 0
+ 2 0
? 1
? 2
'''
