import __main__
import pytest
from main import sum,res,mul,div

def test_sum1():
    assert sum(2,5)==7
    print ("la funcion suma trabaja correctamente")
    
def test_sum2():
    assert sum(3,9)!=7
    print ("la funcion suma trabaja correctamente")

def test_res1():
    assert res(5,3)==2
    print ("la funcion resta trabaja correctamente")
    
def test_res2():
    assert res(4,3)!=2
    print ("la funcion resta trabaja correctamente")
    
def test_mul1():
    assert mul(2,5)==10
    print ("la funcion multiplicación trabaja correctamente")
    
def test_mul2():
    assert mul(3,5)!=10
    print ("la funcion multiplicación trabaja correctamente")
    
def test_div1():
    assert div(10,2)==5
    print ("la funcion división trabaja correctamente")
    
def test_div2():
    assert div(12,2)!=5
    print ("la funcion división trabaja correctamente")
    
if __name__=='__main__':
    test_sum1()
    test_sum2()
    test_res1()
    test_res2()
    test_mul1()
    test_mul2()
    test_div1()
    test_div2()
   
    
    