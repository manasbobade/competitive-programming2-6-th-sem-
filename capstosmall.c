#include <stdio.h>
#include <string.h>

int main() {
   char s[100];
   int i;
   printf("\nEnter a string : ");
   gets(s);

   for (i = 0; s[i]!='\0'; i++) {
       if(s[i]=='A' || s[i]=='E' || s[i]=='I' || s[i]=='O' || s[i]=='U' || s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u')
       {
           continue;
       }
      if(s[i] >= 97 && s[i] <= 122) {
         s[i] = s[i] - 32;
         continue;
      }
      if(s[i] >= 65 && s[i] <= 90) {;
         s[i] = s[i] + 32;
      }
   }
   printf("\nString in Upper Case = %s", s);
   return 0;
}
