# -*- coding: utf-8 -*-
import pytest
from grab_question1 import find_sum

def test_find_sum1():
    array=[1,2,3,3,4,5,5]
    n=6
    result=[(1,5),(1,5),(2,4),(3,3)]
    assert find_sum(array,n)==result

def test_find_sum2():
    array=list(range(1,100))#1-99的数组
    for n in range(3,101):#结果为[(1,n-1),(2,n-2)…]
        i=1
        result=[]
        while i<=int((n-1)/2):
            result.append((i,n-i))
            i=i+1
        assert find_sum(array,n)==result

def test_find_sum3():
    array=[1,1,2,2,3,3,4,4]
    n=6
    result=[(2,4),(2,4),(2,4),(2,4),(3,3)]
    assert find_sum(array,n)==result
    
def test_find_sum4():
    array=[1,1,2,2,3,4,4]
    n=6
    result=[(2,4),(2,4),(2,4),(2,4)]
    assert find_sum(array,n)==result
    
def test_find_sum5():
    array=[1,1,2,2,2,4,4,5,5]
    n=7
    result=[(2,5),(2,5),(2,5),(2,5),(2,5),(2,5)]
    assert find_sum(array,n)==result

def test_find_sum6():
    array=[-3,-3,-2,-1,-1]
    n=-3
    result=[(-2,-1),(-2,-1)]
    assert find_sum(array,n)==result
    
def test_find_sum7():
    array=[-3,-3,-2,-1,1,3]
    n=0
    result=[(-3,3),(-3,3),(-1,1)]
    assert find_sum(array,n)==result
    
def test_find_sum8():
    array=[-3,-3,-2,-1,1,3]
    n=5
    result=[]
    assert find_sum(array,n)==result