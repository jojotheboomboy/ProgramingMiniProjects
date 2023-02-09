//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Author: Josiah Norman
// Homework Question 2
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#include <string.h>
#include <stdio.h>
#define MAX 256

int main()
{
    // this number will be used to check if "exit" was typed 
    int k = 1;

    // primary while loop.
    while (k = 1)
    {
        //allocates 256 bytes to character string.
        char str[MAX];

        //gets the input.
        fgets(str, MAX, stdin);

        //user input will be compared to this statement.
        char strB[] = "exit\n";

        int compare;
        compare = strncmp(strB, str, MAX);
        
        // If the first 4 values of the input do not match, the program will follow this if 	statement. 
        if (compare != 0) 
        {

            // constant that will serve as the tool by which we will parse the input.
            const char d[] = " ";

            //initialize char token variable.
            char *token;

            // Formating and Reprint.
            printf("Line read: %s\n", (str));
            printf("Token(s):\n");

            // gets the first token.
            token = strtok(str, d);

            // variable used to count the amount of tokens.
            int x = 0;

            // iteratively steps through the tokens.
            while (token != NULL)
            {
                printf(" %s\n", token);

                token = strtok(NULL, d);
                
                x++;
            }

            // print and formatting for the amount of tokens that were found.
            printf("%i token(s) read\n\n", (x));
        }

        // If the first 4 values of the input do match, the program will follow this if 		statement.
        else
        {       
            k = 0;
            break;
        }
    }
    return(0);
}