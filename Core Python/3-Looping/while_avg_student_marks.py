max_subj = 0
total = 0
a = []

while max_subj < 5:
    a.append(eval(input("Enter marks for subject: ")))
    total += a[max_subj]
    max_subj += 1

avg = total / 5
