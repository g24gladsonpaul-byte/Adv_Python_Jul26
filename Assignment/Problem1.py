def count_characters(text):
    frequency = {}

    #Convert string to lowercase
    text = text.lower()

    for ch in text:
        if ch.isalpha():
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1
    
    return dict(sorted(frequency.items()))

text = input("Enter a string: ")
print(count_characters(text))