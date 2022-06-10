with open('./task.txt', 'r') as file:
    temp_ll = list()
    count = 0

    for line in file:
        if count % 2 == 0:
            line = line.replace('.','@')
            line = line.replace('-','@')
            line = line.replace(',','@')
            line = line.replace('!','@')
            line = line.replace('?','@')
            temp_ll = [x for x in line.split()]
            temp_ll.reverse()
            print(" ".join(temp_ll))
        count += 1