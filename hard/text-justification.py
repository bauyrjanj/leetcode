def text_just(words, maxlen):
    lst = []
    res = []
    n = 0

    for w in words:

        if len(w) + n + len(lst) > maxlen:
            gaps = (len(lst)-1) or 1
            q, r = divmod(maxlen-n, gaps)

            for i in range(gaps):
                lst[i]+=" "*q + (" " if i<r else "") # reminder (r) is always smaller than the gaps because \
                                                    # if otherwise it would have been divisible by gaps
                                                    # hence the left most side will get extra one space in this case

            res.append("".join(lst))
            n, lst = 0, []

        lst.append(w)
        n+=len(w)

    return res + [" ".join(lst).ljust(maxlen)] if lst else []

if __name__=='__main__':
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    # words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a",
    #                 "computer.", "Art", "is", "everything", "else", "we", "do"]
    # maxwidth = 20
    #
    maxwidth = 16
    res = text_just(words, maxwidth)
    print(res)


