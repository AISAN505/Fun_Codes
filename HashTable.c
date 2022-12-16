#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdint.h>
#include<stdbool.h>

#define MAX_NAME 256
#define TABLE_SIZE 10

typedef struct {
    char name[MAX_NAME];
    int age;
    //....add other stuff later
} person;

person * hash_value[TABLE_SIZE];

unsigned int hash(char *name) {
    int length = strnlen(name, MAX_NAME);
    unsigned int hash_value = 0;
    for(int i = 0; i < length; i++) {
        hash_value += name[i];
        hash_value = (hash_value * name[i]) % TABLE_SIZE;
    }
    return hash_value;
}

void init_hash_table() {
    for(int i = 0; i < TABLE_SIZE; i++) {
        hash_table[i] = NULL;
    }
    //Table is empty
}


void print_table() {
    for(int i = 0; i < TABLE_SIZE; i++) {
        if (hash_table[i] == NULL) {
            printf("\t%i\t---",i);
        } else {
            printf("\t%i\t%s\n", i, hash_table[i]->name);
        }
    }
} 

int main() {
    init_hash_table();
    print_table();
    
    /*printf("Jacob => %u\n",hash("Jacob"));
    printf("Issam => %u\n",hash("Issam"));
    printf("John => %u\n",hash("John"));*/
    return 0;
}
