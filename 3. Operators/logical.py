""" 
to compare two or more comparosons
and
or
not: reverse tthe result, if true makes ut false
"""

# AND
print(5 < 3 and "5" + 10)
# it will give false as
# cond1 and cond2 and cond3; if cond1 is FALSE
# then wont check anything else even if cond2 and cond3 doesnt make sense
# if cond1 is true and other cond does not make sense
# then error

print(5 > 3 and 5 + 10)
# true
# implicit conversion: convert on its own
# 5+10=15 --> truthly
# 5>3: True and 5+10=15 -> Truthly
# true and true is true
