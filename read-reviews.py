# Find reviews and calculate it.
# -----------------------------
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

# Reviews of less than 100 words 
# -----------------------------
# less = []
# for select in data:
#     if len(select) < 100:
#         less.append(select)

# optimized
# -----------------------------
less = [select for select in data if len(select) < 100]
print('Total', len(less), 'less than 100 words')

# good = []
# for select in data:
#     if 'good' in select:
#         good.append(select)

# optimized
# -----------------------------
good = [select for select in data if 'good' in select]
print('Total', len(good), 'have good words')