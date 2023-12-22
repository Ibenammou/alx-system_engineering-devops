#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates five zombie processes and displays
 * messages for each one
 * Return: nothing
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
 * main - main Entry
 * Return: infinity
 */
int main(void)
{
	pid_t child_pid;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", getpid());
	}

	return (infinite_while());
}
