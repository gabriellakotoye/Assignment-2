
import numpy as np
L = 12 #length of the beam in meters
W = 10 #intesity of the load in kN/m
#Question A
#Bending moment(M) and shear force(V) at the first end, x=0
x=0
M = (W*(-6*x**2+6*L*x-L**2))/12
V = W*(L/2-x)
m= 'the bending moment at x=0 is'
v= 'the shear force at x=0 is'
print()
print('(A.1)'+m+str(M)+'and',v+str(V))
#bending moment(M) and shear force(V) at the first end, x=L=12
x=L
M = (W*(-6*x**2+6*L*x-L**2))/12
V = W*(L/2-x)
y= 'the bending moment at x=l is'
z= 'the shear force at x=l is'
print()
print('(A.2)'+m+str(M)+'and',v+str(V))
#Question b
#when the bending moment is zero,we get an expression x**2-Lx + L**2/6 = 0
#from the expression
a = 1
b = -L
c = L**2/6
#Using the almghty formula the two roots are;
discriminant = b**2 - 4*a*c
root_1b = (-b + np.sqrt(discriminant))/2*a
root_2b = (-b - np.sqrt(discriminant))/2*a
print()
print('(b) The pointsof contra-flexure are {0} and {1}'. format(root_1b,root_2b))
#Question c
#when the shear force is zero,x = L/2
x = L/2
print()
print('(c) The point at which V=0 is {}'. format(x))
#Question d
r = 0
s = 0.01
t = L + s
x = np.arange(r,s,t)
M = (W*(-6*x**2 + 6*L*x-L**2))/12
print()
print('(d) Using the initialized variable,the bending moment at each step in the array is {0}'.format(M))
#Question e
V = W*(L/2- x)
print()
print('(e) The shear force for each step along the span is {}'. format(V))
#Question f
#let the absolute value of M = AM
#also let the minimum AM = m_AM
AM = abs(M)
m_AM = min(AM)
#when the bending moment is m_AM, we get an expression x**2 - L*x + (L**2/6)+(2*m_AM)/w = 0
#from the above expression
a = 1
b = -L
c = (L**2/6)+(2*m_AM)/W
#using the almighty formula the two roots  are;
discriminant = b**2 - 4*a*c
root_1f = (-b + np.sqrt(discriminant))/2*a
root_2f = (-b - np.sqrt(discriminant))/2*a
print()
print('(f) The point along L at which the absolute values of the bending moment array is minimum are {0} and {1}'. format(root_1f,root_2f))
#Question g
#let the relative errors be r_e
r_e1 = ((root_1b - root_1f)/root_1b*100)
r_e2 = ((root_2f - root_2b)/root_2f*100)
print()
print('(g) The relative errors between estimated points of contra-flexure are {0}% and {1}%'. format(r_e1,r_e2))
#Question h
#let the maximum bending moment be max_M and the minimum bending moment be min_M
#for the maximum
max_M = max(M)
#when the bending moment is max_M, we get an expression x**2 -L*x +(L**2/6)+(2*max_M)/w = 0
a = 1
b = -L
c = (L**2/6)+(2*max_M)/W
#Using the almighty formula the two roots are;
discriminant = b**2 - 4*a*c
root_1 = (-b + np.sqrt(discriminant))/2*a
root_2 = (-b - np.sqrt(discriminant))/2*a
print()
print('(h.1) the points at which the maximum bending moment occur are {0} and {1}'. format(root_1,root_2))
#for the minimum
min_M = min(M)
#when the bending moment is min_M, we get an expression x**2-Lx + (L**2//6)+(2*min_M)/W = 0
a = 1
b = -L
c = (L**2//6)+(2*min_M)/W
#Using the almighty formula the two roots are;
discriminant = b**2 - 4*a*c
root_1 = (-b + np.sqrt(discriminant))/2*a
root_2 = (-b - np.sqrt(discriminant))/2*a
print()
print('h.2) The points at which the minimum bending moment occur are {0} and {1}'. format (root_1,root_2))















































