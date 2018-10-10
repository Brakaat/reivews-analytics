data = []
count = 0
with open('reviews.txt', 'r') as file:
    for line in file:
        data.append(line)
        # count += 1
        # if count % 1000 == 0:
        #     print(len(data))
print('Total', len(data), 'reviews')
#print(len(data[0]))
sum_len = 0
for avg in data:
    sum_len += len(avg)
print('Total', sum_len, 'words')
print('Average is', sum_len/len(data), 'words')