#include <time.h>
#include <stdlib.h>
#include <stdio.h>

void main() {
    // Fetch the system's date and time
    srand(time(NULL));
    // Setting rand1 to maximus number RAND_MAX
    int rand1 = rand();
    printf("Random number between 0 and %d: %d\n", RAND_MAX, (int)rand1);
    int min = 0, max = 100;
    float rand2 = (float)rand() * max / RAND_MAX + 1;
    int round = (int)rand2;
    printf("Random number between %d and %d: %d (%f)\n", min, max, round, rand2);
    /* This somehow does not end up printed. Only first printf does.*/
    time_t T = time(NULL);
    struct tm tm = *localtime(&T);
    printf("%02d-%02d-%04d %02d:%02d:%02d\n", tm.tm_mday, tm.tm_mon, tm.tm_year, tm.tm_hour, tm.tm_min, tm.tm_sec);
    return;
}
