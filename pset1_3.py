# word = 'gkdbeukeziwgwkhcoqq'
# word = 'abcbcd'
word = 'zyxwvutsrqp'


# Returns longest substring in s where each letter is alphabetical order
def longest_substring(s):
    # Length of substring
    longest_count = 1
    # Starting index of substring
    longest_index = 0
    # Loop through word
    for letter in range(len(s)-1):
        # Temporary count of length
        count = 1
        # Iterate through remainder of string
        for i in range((letter+1), len(s)):
            # Check if alphabetical
            if s[i-1] <= s[i]:
                count += 1
                # Update variables if current count is the longest
                if count > longest_count:
                    longest_count = count
                    longest_index = letter
            else:
                break

    return s[longest_index:longest_index+longest_count]


longest_str = longest_substring(word)
print('Longest substring in alphabetical order is: ' + str(longest_str))
