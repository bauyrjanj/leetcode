'''
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible.

If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

* no padding at the beginning and end of the line?


Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

["This", "is", "an", "example", "of", "text", "justification."]


1. reverse the wordlist -> rev = ["justification.", "text", "of", "example", "an", "is", "This"]

2. pop from rev

3. count the characters of popped token

4. if len(new_string)+1+len(popped_token)<=width
                 add space -> new_string+=' '
        then add the token -> new_string+=popped_token
   else:
        rev.append(popped_token)
        output.append(new_string)
        new_string = ''

5. Add extra spaces

add_space = width - len(last_element) -> calculate additional space to be padded

figure out where to add the additional space
                              -> distribute the additional space within words evenly
                              -> if can't distribute evenly, then padd more spaces in the left than right
                              -> last token to be left justified - pad the end of the token




'''

def text_justification(words, maxlen):
    temp = []
    linelen = 0
    i = 0
    j = 1
    N = len(words)
    result = []
    final = []

    while j<=N-1:
        linelen+=len(words[i])
        if linelen+1+len(words[j])<=maxlen:
            j+=1
        else:
            linelen = 0
            temp.append(' '.join(words[i:j]))
            i=j
            j+=1
        if j==N-1:
            temp.append(' '.join(words[i:]))

    for p, token in enumerate(temp):
        diff = maxlen-len(token)
        result = token.split(' ')
        spaces = len(result)-1

        if spaces==0:
            result[0] = result[0].ljust(len(result[0])+diff)
        elif p==len(temp)-1:
            result[-1] = result[-1].ljust(len(result[-1]) + diff)
        elif diff%spaces==0:
            extra_spaces = diff//spaces
            for i in range(len(result)-1):
                result[i]+=' '*extra_spaces
        else:
            r = diff%spaces
            extra_spaces = diff//spaces
            for k in range(len(result)-1):
                if k==0:
                    result[k]+=' '*(extra_spaces+r)
                result[k] += ' ' * extra_spaces

        final.append(''.join(result))

    return final


if __name__=='__main__':
    # words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a",
                    "computer.", "Art", "is", "everything", "else", "we", "do"]
    maxwidth = 20

    # maxwidth = 16
    res = text_justification(words, maxwidth)
    print(res)









