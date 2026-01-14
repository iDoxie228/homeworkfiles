files = ['1.txt', '2.txt', '3.txt']
file_data = []
for file in files:
    with open(file) as f:
        data = f.readlines()
        file_data.append((file, len(data), data))
file_data.sort(key=lambda x: x[1])
print(file_data)

with open('res_txt', 'w') as ff:
    for file, count, lines in file_data:
        ff.write(f'{file}\n')
        ff.write(f'{count}\n')
        ff.writelines(lines)
        ff.write('\n')
        ff.write('\n')
        
        

