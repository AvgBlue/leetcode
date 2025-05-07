#include <stdio.h>
#include <string.h>

char* capitalizeTitle(char* title) {\
    int len=strlen(title)
    for(int i=0;i<len;){
        int j=i;
        while(title[j]!='\0'&&title[j]!=' '){
            title[j]+=('A'<=title[j]&&title[j]<='Z')?'a'-'A':0;
            j++;
        }
        int wordlen=j-i;
        if(wordlen>2){
            title[i]-='a'-'A';
        }
        i=j+1;
        
    }
    return title;
}


int main() {
    char title[] = "capiTalIze tHe titLe";
    printf("Original Title: %s\n", title);
    printf("Capitalized Title: %s\n", capitalizeTitle(title));
    return 0;
}