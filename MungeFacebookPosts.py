import regex as re
import numpy as np


def randomSwapLetters(word, swapCount=1):
    rng = np.random.default_rng()
    # Create a sorted list of indexes into characters to be swapped within the word
    # We want to draw 2 distinct positions for each swap
    # This explains why we multiply the swapCount by 2
    # and also why we don't want to do a select with replacement
    idx = sorted(
        list(rng.choice(
            np.array(list(range(len(word)))), size=2*swapCount, replace=False
        ))
    )
    # Swap at least 1 set of characters
    munged = word[:idx[0]] + word[idx[1]] + \
        word[idx[0] + 1: idx[1]] + word[idx[0]] + word[idx[1]+1:]
    if swapCount > 1:
        # For longer words, we will swap 2 sets of characters
        munged = munged[:idx[2]] + munged[idx[3]] + \
            munged[idx[2] + 1: idx[3]] + munged[idx[2]] + munged[idx[3]+1:]
    return munged


def main():
    print("Enter text to be munged/mangled for posting to Facebook:\n")
    # Hello World! This is an attempt to munge text when posting to Facebook, specifically to mangle words that ***might*** be "misconstrued" as abusive language.

    # Collect the text for munging
    txtInput = input()

    # Split entered text on space characters
    splitWords = txtInput.split()

    # Using regular expression, grab any leading (pre) or trailing (post)
    # text that is non-alpha from each word, using list comprehension
    prepostfix = [
        (re.search(r'(^[^A-Za-z]*)', x)[0], re.search(r'([^A-Za-z]*)$', x)[0])
        for x in splitWords
    ]

    # Using regular expression, grab any text between the leading (pre) or trailing (post)
    # text that is non-alpha from each word, using list comprehension
    words = [
        re.sub(r'(^[^A-Za-z]*)', '', re.sub(r'([^A-Za-z]*)$', '', x))
        for x in splitWords
    ]

    # Using only the alpha-ish text (note - we may still have non-alpha in the middle of a word)
    # perform the munging operation by calling the function we defined above on each
    # word in the list, again using list comprehension to assemble the list
    # The function randomSwapLetters is called with different parameters
    # depending on the length of the word being processed within the list.
    munged = [
        w if len(w) < 4
        else w[0] + randomSwapLetters(w[1:-1], 1) + w[-1] if len(w) < 12
        else w[0] + randomSwapLetters(w[1:-1], 2) + w[-1]
        for w in words
    ]

    # After munging each word, assemble the list back into a line of text
    # which will also include adding any leading or trailing characters
    # that were in the original "word".
    mungedText = ' '.join([
        prepostfix[i][0] + munged[i] + prepostfix[i][1]
        if munged[i] != ''
        else prepostfix[i][0]
        for i in range(len(munged))
    ])

    # Print the result back to the user
    print(mungedText)


if __name__ == "__main__":
    main()
