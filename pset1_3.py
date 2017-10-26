# word = 'gkdbeukeziwgwkhcoqq'
# word = 'abcbcd'
word = 'zyxwvutsrqp'


def longest_substring(s):
    longest_count = 0
    longest_index = 0
    for letter in range(len(s)-1):
        count = 1
        for i in range((letter+1), len(s)):
            if s[i-1] <= s[i]:
                count += 1
                if count > longest_count:
                    longest_count = count
                    longest_index = letter
            else:
                break

    return s[longest_index:longest_index+longest_count]


longest_str = longest_substring(word)
print('Longest substring in alphabetical order is: ' + str(longest_str))
