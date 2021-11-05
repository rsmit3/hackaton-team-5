import json

# Using readlines()
def run():
    inputFile = '../data/LidarData.txt'
    outputFile = '../data/LidarData.json'
    file1 = open(inputFile, 'r')
    Lines = file1.readlines()
    # Strips the newline character
    nr=0
    dct={}
    new=False
    for line in Lines:
        if line.split('theta')[0] != 'S  ' and len(line.split('theta'))>1:
            splitted=line.split(':')
            angle = float(splitted[1].split(' ')[1])
            if angle>0 and angle<300:
                if not new:
                    if nr !=0:
                        dct[nr] = listje
                    nr += 1
                    new = True
                    listje=[]
            else:
                new = False
            distance = float(splitted[2].split(' ')[1])
            listje.append([angle,distance,0])

    with open(outputFile, 'w') as outfile:
        json.dump(dct, outfile)

if __name__ ==  "__main__":
    run()
