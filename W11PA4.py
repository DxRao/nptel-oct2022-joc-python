int checkPrime(int num, int i)
{
    if (i == 1)
        return 1;
    else
       if (num % i == 0)
         return 0;
       else
         return checkPrime(num, i - 1);
}
