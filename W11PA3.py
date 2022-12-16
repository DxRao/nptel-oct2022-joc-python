#Composite numbers for a given number is nothing but those other than the prime numbers for any given number.

num1=int(input())
num2=int(input())

count=0
num =num1

for x in range(num1, num2+1):
    for a in range(2, num):
        if num%a==0:
            count+=1
        if count==1:
            print(num)            
            break;
    num = num +1
    count =0
    

'''
Week 11: Programming Assignment 3
Due on 2022-10-13, 23:59 IST
Write a program which takes two integer a and b and prints all composite numbers between a and b. (both numbers are inclusive)

Input:
10
20

Output:
10
12
14
15
16
18
20

'''





'''
# Unmatched old semester Weekly -PA-11 programming  assignment.

while(x0<xn)
    {
        m1=func(x0,y0);
        m2=func((x0+h/2.0),(y0+m1*h/2.0));
        m3=func((x0+h/2.0),(y0+m2*h/2.0));
        m4=func((x0+h),(y0+m3*h));
        m=((m1+2*m2+2*m3+m4)/6);
        y0=y0+m*h;
        x0=x0+h;
    }
    printf("y=%.4f\n",y0);  // Final output
    return 0;
}

float func(float x,float y)
{
    float m;
    m=(x*(x+1)-3*y*y*y)/10;
    return m;
}


'''
