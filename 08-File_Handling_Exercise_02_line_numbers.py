with open('./task.txt', 'r') as file, open('./out_task.txt', 'w') as out_file:
    count = 0
    for line in file:
        count += 1
        punctuation_count = 0
        letter_count = 0
        for ch in line:
            if ch in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
                punctuation_count += 1
            elif ch.isalpha():
                letter_count += 1
        out_file.write(f'Line {count}: {line[:-1]} ({letter_count})({punctuation_count})\n')
