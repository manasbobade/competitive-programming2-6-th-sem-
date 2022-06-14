// Online C compiler to run C program online
#include <stdio.h>

int main() {
   char s[100];
   char tomatch[100];
   int i;
   int j;
   int occurances=0;
   printf("\nEnter a string : ");
   gets(s);
   printf("\nEnter a string to match : ");
   gets(tomatch);
   
   for(i=0;s[i]!='\0';i++)
   {
       if(s[i]==tomatch[0])
        {
            int flag=0;
            for(j=0;tomatch[j]!='\0';j++)
                {
                    if(tomatch[j]!=s[i+j])
                        {
                        flag=1;
                        break;
                        }
                }
            if(flag==0)
                {
                    occurances++;
                
                }
        }
   }
   printf("number of occurances of string\"%s\" in \"%s\" is =%d",tomatch,s,occurances);
}
