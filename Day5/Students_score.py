scores = [100 , 80 , 7 , 6 , 87 , 772, 22 , 63, 12 ]

# total_score = sum(score)
# print(total_score)

# sum = 0
# for num in score:
#     sum += num
#     print(sum)

# print(max(score))

max_score  = 0

for score in scores:
    if score > max_score:
        max_score = score

print(max_score)