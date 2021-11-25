import regex as re
import numpy as np


def randomSwapLetters(word, swapCount=1):
    rng = np.random.default_rng()
    # Create a sorted list of indexes into characters to be swapped within the word
    # We want to draw 2 distinct positions for each swap
    # This explains why we multiply the swapCount by 2
    # and also why we don't want to do a select with replacement
    # We should also try to avoid swapping two letters that are identical for each other
    # For example in the word "science" that characters in positions 1 and 5 are the same "c"
    # At the same time, there may be words the no matter how much we try to swap, will never succeed
    # For example the word "need" will never be anything other than "need"
    # (since we preserve first and last characters in their respective positions)
    loopMax = 10
    i = 0
    while True:
        i += 1
        idx = sorted(
            list(rng.choice(
                np.array(list(range(len(word)))), size=2*swapCount, replace=False
            ))
        )
        if i >= loopMax:
            break
        else:
            if word[idx[0]] != word[idx[1]]:
                if swapCount > 1:
                    if word[idx[2]] != word[idx[3]]:
                        break
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

    # Get a list of "delimiter" characters (basically anything non-alpha) from the input
    splitReChars = list(re.sub(r'[A-Za-z]', '', txtInput))

    # Convert this list into a unique set of characters, then join them to create a regex pattern
    splitPattern = ''.join(list(set(splitReChars)))
    splitPattern = re.sub(r'([\[\]\-\(\)])', r'\\\1', splitPattern)

    # and use this pattern to extract only the words from the input
    splitReWords = re.split('[' + splitPattern + ']', txtInput)

    # Using the words (composed of alpha-only) in the input text
    # perform the munging operation by calling the function we defined above on each
    # word in the list, using list comprehension to assemble the list
    # The function randomSwapLetters is called with different parameters
    # depending on the length of the word being processed within the list.
    munged = [
        w if len(w) < 4
        else w[0] + randomSwapLetters(w[1:-1], 1) + w[-1] if len(w) < 12
        else w[0] + randomSwapLetters(w[1:-1], 2) + w[-1]
        for w in splitReWords
    ]

    # After munging each word, assemble the list back into a line of text
    # by interspacing the separators between each word. We do this by joining
    # pairs of word + delimiter and then adding the final word at the end
    # There will always be precisely one more word than there are delimiters.
    mungedText = ''.join([
        munged[i] + splitReChars[i]
        for i in range(len(splitReChars))
    ]) + munged[-1]

    # Print the result back to the user
    print(mungedText)


if __name__ == "__main__":
    main()
