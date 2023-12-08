def find_times(threshold):
    with open("input.txt", "r") as f:
        lines = f.readlines()
    times = []
    for line in lines:
        time, value = line.split()
        if int(value) > threshold:
            times.append(time)
    return times

threshold = int(input("Введіть допустимий ліміт: "))
times = find_times(threshold)
print("Часи, коли виміри перевищили задане значення:")
for time in times:
    print(time)
