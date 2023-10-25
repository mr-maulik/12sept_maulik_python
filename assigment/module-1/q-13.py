#Write a Python program to count the number of characters (character frequency) in a string 

t_str = "hello python"
 
all_freq = {}
 
for i in t_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print("Count of all characters in hello python is :\n "
      + str(all_freq))