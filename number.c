#include <stdio.h>

void main()
{
    int n,i=0;
    scanf("%d",&n);
    if (n<500)
    {
    
    long int ar[n];
    for(i=0;i<n;i++){
       scanf("%d",&ar[i]);
    }
    long int bit[n];
    for (i = 0; i < n; i++)
    {
        int x=ar[i];
        int t=x,d,lar=0,small;
        while (t>0)
        {
            d=t%10;
            if(lar<d){
                lar=d;
            }
            t=t/10;  
        }
        t=x;
        small=t%10;
       while (t>0)
        {
            
            d=t%10;
            if(small>d){
                small=d;
            }
            t=t/10;  
        }
        int sum= small*7 + lar*11;
        sum=sum%100;
        bit[i]=sum;
    }
    int count1=0,count2;
    int k[9];
    for (i = 0; i < 9; i++)
    {
        k[i]=0;
    }
    
    for (i = 0; i < n; i++)
    {
        int x=bit[i];
        int d=x/10;
        count2=0;
        for (int j = i+2; j < n; j=j+2)
        {
            int f=bit[j];
            f=f/10;
            if(d==f)
            {
                if(k[d]<2)
                  {
                      k[d]=k[d]+1;
                      count2++;
                }
            }
        }
        count1=count1+count2;
    }
    printf("%d",count1);
    }
}