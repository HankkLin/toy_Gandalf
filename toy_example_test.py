#!/usr/bin/env python
# coding: utf-8
# %%

# %%


import toy_example


# %%


Answer = toy_example.returnAnswer("Hello.", "Hard")
password = toy_example.returnPassword()
print("The password is: "+ password + "\n")
for word in Answer.split():
    print(word)
    assert not word == password, "The answer include password \"{}\"".format(word)
print("All clear! The response doesn't include the answer.")


# %%




