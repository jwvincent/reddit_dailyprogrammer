def Pile_of_Paper(*arg):
    canvas = []
    counts = []
#    print(arg[0][0][1])
    for i, v in enumerate(arg):
        counts.append([i,0])
        if len(v) == 2:
#            print (len(v))
#            print (i)
            for j in range(arg[0][1]):
                canvas.append([])
            for idx, val in enumerate(canvas):
                for k in range(0, arg[0][0]):
                    canvas[idx].append(0)
        if len(v) == 5:
            for j in range(arg[i][2], arg[i][4]):
                for k in range(arg[i][1], arg[i][3]):
                    canvas[j][k] = arg[i][0]
#        else:
#            return False
#            print ("invalid input")
#    print canvas
    for i, v in enumerate(canvas):
        for j in canvas[i]:
            for ind, v in enumerate(counts):
                if ind == j:
                    counts[ind][1] += 1
                    break
    return counts

print (Pile_of_Paper([4,4],[1,0,0,2,2],[2,2,2,4,4],[3,0,2,2,4]))
