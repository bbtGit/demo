#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''-----------------------------------------------
@File       : exc
@Description:  
@Author     ：bbt
@Date       ：2020/4/24 1:08
-----------------------------------------------'''
class Person:
    def __init__(self, name, sex, birthday):
        self.name = name
        self.sex = sex
        self.birthday = birthday

    def say(self, word):
        print(f'{self.name}说:"{word}"')


zhangsan = Person("张三", "男", "20120345")
zhangsan.say('你好')