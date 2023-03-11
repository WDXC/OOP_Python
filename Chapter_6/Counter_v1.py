from collections import  Counter
def letter_frequency(sentence):
    return Counter(sentence)

responses = [
    "vanilla",
    "chocolate",
    "vanilla",
    "vanilla",
    "caramel",
    "strawberry",
    "vanilla"
]

print("The children voted for {} ice cream".format(
    Counter(responses).most_common(1)[0][0]
))