import re

text = """Giraffes have aroused
 the curiosity of __PLURAL_NOUN__
 since earliest times. The
 giraffe is the tallest of all
 living __PLURAL_NOUN__, but
 scientists are unable to
 explain how it got its long
 __PART_OF_THE_BODY__. The
 giraffe's tremendous height,
 which might reach __NUMBER__
 __PLURAL_NOUN__, comes from
 it legs and __BODYPART__.
"""

def mad_libs(string):
    hint = re.findall("__.*?__", string)
    if hint is not None:
        for word in hint:
            q = input("Enter a {}".format(word))
            string = string.replace(word, q, 1)
        print("/n")
        string = string.replace("/n", "")
        print(string)
    else:
        print("invalid Stirng")

mad_libs(text)