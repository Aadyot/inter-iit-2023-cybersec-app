#!/usr/bin/env python

from signer import Signer

sgn = Signer()

# You can NOT use the [__sign] or [__verify] function in [signer.py].
# Your solution should work for any value of [key] and therefore should not be a
# hardcoded solution.

# Your solution HERE.

# The final and the only print statement in the program should print out
# "Congratulations, you did it!" after a successful execution.
# There should be no other print statements in the program and you cannot
# hardcode this string to be printed.




def str2byte(s):
    return s.encode("utf-8").hex()

#InterIIT-2023 is 13 chars, so 13 bytes 

print(sgn.execute("sign", str2byte("InterIIT-2023")))

