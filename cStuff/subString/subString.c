#include <stdio.h>
#include <string.h>

int main() {
    char str1[100], str2[100];
    int i, j;

    printf("Enter the Big Pattern string: ");
    fgets(str2, 100, stdin);
    str2[strcspn(str2, "\n")] = '\0';
    
    printf("Enter the SubString: ");
    fgets(str1, 100, stdin);
    str1[strcspn(str1, "\n")] = '\0';

    int len1 = strlen(str1);
    int len2 = strlen(str2);

    if (len1 > len2) {
        printf("%s is not a substring of %s\n", str1, str2);
        return 0;
    }

    for (i = 0; i <= len2 - len1; i++) {
        for (j = 0; j < len1; j++) {
            if (str1[j] != str2[i + j]) {
                break;
            }
        }
        if (j == len1) {
            printf("%s is a substring of %s\n", str1, str2);
            return 0;
        }
    }
    printf("%s is not a substring of %s\n", str1, str2);
    return 0;
}
