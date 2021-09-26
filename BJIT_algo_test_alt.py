participant_num = int(input())

arr = []
single_arr = []
total_score = 0
for i in range(participant_num):
    x = int(input())
    y = int(input())
    z = int(input())

    sum_num = x + y + z
    arr.append((i, sum_num))
    total_score += sum_num
    single_arr.append(sum_num)


def sort_tuple(tup):

    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):

        for j in range(0, lst-i-1):
            if (tup[j][1] < tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup


min_val = min(single_arr)
max_val = max(single_arr)
top_scorer = single_arr.index(max_val) + 1
lowest_scorer = single_arr.index(min_val) + 1

sorted_arr = sort_tuple(arr)  # sorted by rank


participants_no = [position+1 for (position, score) in sorted_arr]

rank = 1
for position in participants_no:
    print("Participant" + str(position) + " = " + str(rank))
    rank += 1

print("Participant" + str(top_scorer) + " scored top = " + str(max_val))
print("Participant" + str(lowest_scorer) + " scored lowest = " + str(min_val))
