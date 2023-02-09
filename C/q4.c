#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/time.h>

int main(int argc, char * argv[])
{
    pid_t pid = fork();
    if (pid == 0)
    {
        char * exec_args[4] = {argv[1], argv[2], argv[3], NULL};
        printf("In Child %d: ", getpid());
        fflush(stdout);
        execvp(exec_args[0], exec_args);
    }
    else 
    {
        wait(NULL);
    }
    exit(0);
}


