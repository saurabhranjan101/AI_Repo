#Count word frequency in a sentence.

sentence = "this is a test this is only a test sorry"
#output -> this -2, is - 2, test-2
freq = {}
words = sentence.split()
for word in words:
    freq[word] = freq.get(word,0)+1
print(freq)


dict1 = {
"Name":"Saurabh",
"Roll Number" :35
}
print(dict1.items())
print(dict1.get("Name")) ##Get you value for key you passed
print(dict1.keys())
print(dict1.values())