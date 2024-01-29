#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Runs an infinite loop
 * Return: Always returns 0
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - Creates 5 zombie processes
 * Return: Always returns 0
 */
int main(void)
{
    int zombies_created = 0;
    pid_t pid;

    while (zombies_created < 5)
    {
        pid = fork();
        if (!pid)
            exit(0); // Child exits immediately to become a zombie
        printf("Zombie process created, PID: %i\n", (int)pid);
        zombies_created++;
    }

    if (pid != 0)
        infinite_while(); // Parent enters infinite loop to keep zombies alive

    return (0);
}
