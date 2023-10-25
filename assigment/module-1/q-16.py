sample = "hii buddy how are you buddy"

sample = sample.lower()
words = sample.split()
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for key, value in count.items():
    print(key, value)
