# Input Section
n = int(input())  # Taking Participants number input

scores = []
# Taking Participants marks input
for _ in range(n):
    x, y, z = input("Enter a three value: ").split()
    scores.append(int(x) + int(y) + int(z))


# Calculate Avg Score
def calc_avg_score(arr):
    arr_sum = 0
    avg = 0
    for num in arr:
        arr_sum += num

    return "{0:.2f}".format(arr_sum / len(arr))


# Print Participants with Position
def print_partici_position(arr):
    parici_positions = []  # this array is to test
    arr_len = len(arr)

    # here I will compare i index with every other arr elements and get its position'
    for i in range(arr_len):
        parici_position = 1
        for j in range(arr_len):
            if arr[i] < arr[j]:
                parici_position += 1

        # now what if same score gained by another participants?
        while parici_position in parici_positions:
            parici_position += 1
        parici_positions.append(parici_position)
        print("Participant" + str(i + 1), " = ", parici_position)


def print_top_lowest_score(arr):
    top_score = max(arr)
    lowest_score = min(arr)

    top_participant = (arr.index(top_score)) + 1
    lowest_participant = arr.index(lowest_score)

    print("Participant" + str(top_participant) + "scored top", "= ", top_score)
    print("Participant" + str(lowest_participant) +
          "scored lowest", "= ", lowest_score)


# Output Sections
print_partici_position(scores)
print_top_lowest_score(scores)
print(f"AVG score = {calc_avg_score(scores)}")
