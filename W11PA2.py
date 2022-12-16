S = input().split('#')
S = sorted(S, reverse=True)
print("#".join(S), end="")


'''
Week 11: Programming Assignment 2
Due on 2022-10-13, 23:59 IST
Write a program that accepts a hash-separated sequence of words as input and prints the words in a hash-separated sequence after sorting them alphabetically in reverse order.

Input:
hey#input#bye

Output:
input#hey#bye


Input	Output
Test Case 1	
hey#input#bye
        input#hey#bye
Test Case 2	
which#of#us#ever#undertakes#laborious#physical#exercise
        which#us#undertakes#physical#of#laborious#exercise#ever
Test Case 3	
At#vero#eos#et#accusamus#et#iusto#odio#dignissimos#ducimus
        vero#odio#iusto#et#et#eos#ducimus#dignissimos#accusamus#At




'''

'''
# Unmatched different previous week -  PA 11 Programming assignment.

int i;
float h,x, sum=0;  
if(b>a)
  h=(b-a)/n;
  else
  h=-(b-a)/n;
  for(i=1;i<n;i++){
    x=a+i*h;
    sum=sum+func(x);
  }
  integral=(h/2)*(func(a)+func(b)+2*sum);
  printf("The integral is: %0.6f\n",integral);
  return 0;
}

float func(float x)
{
  return x*x;
  }

'''
