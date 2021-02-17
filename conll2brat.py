import sys


if __name__ == "__main__":
    filename = sys.argv[1]

    f = open("{}.preds".format(filename), "r")
    Lines = f.readlines()
    lines = []
    # Split lines to two groups for MENTIONS and COREF

    for line in Lines:
        l = line.strip()
        if len(l)!=0:
            lines.append(l)

    d = {}
    #d_start_word = {}
    #d_end_word ={}
    d_start = {}
    d_end = {}
    p = 0
    for i in range(len(lines)):
        if p == 0:
            if i > 0 and i < (len(lines)-1):
                line = lines[i].split('\t')
                if len(line) == 13:
                    coref_index = line[12]
                    if coref_index[0]=='(' and coref_index[len(coref_index)-1] == ')':
                        key = coref_index[1:len(coref_index)-1]
                        if key not in d:
                            d[key] = [line[3]]
                            s = 0
                            for i in range(1,i):
                                s += len(lines[i].split('\t')[3])+1
                            d_start[key] = [s]
                            s += len(lines[i+1].split('\t')[3])
                            d_end[key] = [s]
                        else:
                            d[key].append(line[3])
                            s = 0
                            for i in range(1,i):
                                s += len(lines[i].split('\t')[3])+1
                            d_start[key].append(s)
                            #print(lines[i+1].split('\t')[3])
                            s += len(lines[i+1].split('\t')[3])
                            #print(s)
                            d_end[key].append(s)
                    elif coref_index[0]=='(' and coref_index[len(coref_index)-1] != ')':
                        key = coref_index[1:len(coref_index)]
                        temp = [lines[i].split('\t')[3]]
                        count = 1
                        p -= 1
                        while len(lines[i+count].split('\t')) != 13 or lines[i+count].split('\t')[12][len(lines[i+count].split('\t')[12])-1] != ')':
                            temp.append(lines[i+count].split('\t')[3])
                            count += 1
                            p -=1
                        temp.append(lines[i+count].split('\t')[3])
                        if key not in d:
                            d[key] = [" ".join(temp)]
                            s = 0
                            for i in range(1,i):
                                s += len(lines[i].split('\t')[3])+1
                            d_start[key] = [s]
                            s += len(" ".join(temp))
                            d_end[key] = [s]
                        else:
                            d[key].append(" ".join(temp))
                            s = 0
                            for i in range(1,i):
                                s += len(lines[i].split('\t')[3])+1
                            d_start[key].append(s)
                            s += len(" ".join(temp))
                            d_end[key].append(s)
        else:
            p += 1

    f = open("{}.ann".format(filename), "w")
    c = 1
    r = 1
    for i in d.keys():
        idx = []
        for j in range(len(d[i])):
            idx.append(c)
            f.write('T'+str(c)+'\t'+'PER'+' '+ str(d_start[i][j]) + ' ' + str(d_end[i][j])+'\t'+d[i][j]+'\n')
            c+=1
        for k in range(len(idx)-1):
            f.write('R'+str(r)+'\t'+'Coreference' + ' ' + 'Arg1:' + 'T'+str(idx[k]) + ' ' + 'Arg2:' + 'T'+str(idx[k+1])+'\n')
            r += 1
    f.close()
