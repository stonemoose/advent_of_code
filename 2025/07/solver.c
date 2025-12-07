#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char *line = NULL;
    size_t len = 0;
    getline(&line, &len, stdin);

    int line_length = strlen(line) - 1;
    unsigned long *beams = malloc(line_length * sizeof(long));
    beams[line_length/2] = 1;

    int splits = 0;
    unsigned long *next_beams = malloc(line_length * sizeof(long));
    while(getline(&line, &len, stdin) != -1) {
        memset(next_beams, 0, line_length * sizeof(long));
        for (int i = 0; i < line_length; i++) {
            if (line[i] == '^') {
                if (beams[i] != 0) {
                    splits++;
                    next_beams[i-1] += beams[i];
                    next_beams[i+1] += beams[i];
                }
            } else {
                next_beams[i] += beams[i];
            }
        }
        unsigned long *tmp = beams;
        beams = next_beams;
        next_beams = tmp;
    }

    printf("Part 1: %d\n", splits);
    unsigned long quantum_timelines = 0;
    for (int i = 0; i < line_length; i++) {
        quantum_timelines += beams[i];
    }
    printf("Part 2: %lu\n", quantum_timelines);
    free(line);
    free(beams);
    free(next_beams);
}
