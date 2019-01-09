#!/usr/bin/python
# -*- coding: UTF-8 -*-
import string
import random


class LetterVerificationCode:
    def __init__(self, num_of_code=20, save_path=''):
        self.save_path = save_path
        self.num_of_code = num_of_code

    def _write_img(self):
        img_w , img_h = 50, 10
        pos_cx = [10, 20, 30, 40]
        pos_cy = 5



    def _vercode_gen(self):
        base_str = string.ascii_letters + string.digits
        key = [random.choice(base_str) for i in range(4)]
        return "".join(key)

    def vercode_gen(self):
        keys = []
        for i in range(self.num_of_code):
            # keys.append(self._vercode_gen())

        #return keys


if __name__ == "__main__":
    ac = LetterVerificationCode(save_path='./')
    ac.vercode_gen()
