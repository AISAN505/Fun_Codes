/* File: buggy.c */
#include <stdio.h>
#include <stdint.h>

uint32_t w, x, y, z;

uint32_t xorshift128(void) {
    uint32_t t = x;
    t ^= t << 11U;
    t ^= t >> 8U;
    x = y; y = z; z = w;
    w ^= t;
    return w;
}

int main() {
    xorshift128();
}
