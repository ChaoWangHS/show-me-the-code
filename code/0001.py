#!/usr/bin/python
# -*- coding: UTF-8 -*-
import string
import random


class ActivationCode:
    def __init__(self, ac_code_len=20, num_of_code = 200):
        self.code_len = ac_code_len
        self.num_of_code = num_of_code

    def _key_gen(self):
        base_str = string.ascii_letters + string.digits
        key = [random.choice(base_str) for i in range(self.code_len)]
        return "".join(key)

    def key_gen(self):
        keys = []
        for i in range(self.num_of_code):
            keys.append(self._key_gen())
        return keys


if __name__ == "__main__":
    ac = ActivationCode(ac_code_len=10)
    list_ = ac.key_gen()
    assert len(list_) == ac.num_of_code
    print(list_)
