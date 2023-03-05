#include<stdio.h>
#include<math.h>    //  As the name suggests, it's a math library
#include<setjmp.h>  // This library is for custume exceptions

double add(double x, double y) {return x + y;};
double sub(double x, double y) {return x - y;};
double mul(double x, double y) {return x * y;};
double dIv(double x, double y) {return x / y;};

// Setting an exception message as 'buf'
jmp_buf buf;
// Function to raise an exception
void raise_an_exception() {
    longjmp(buf, 1);
}

int main() {
    
    char operation;
    double x, y;
    double result;
    
    printf("Select the operation you want (+ - * /) : ");
    scanf("%c", &operation);
    printf("Type two real numbers :");
    scanf("%lf %lf", &x, &y);
    // Begin the calculations
    switch(operation) {
        case '+':
            result = add(x, y);
            break;
        case '-':
            result = sub(x, y);
            break;
        case '*':
            result = mul(x, y);
            break;
        case '/':
            result = dIv(x, y);
            break;
        default:
            printf("Enter a valid operation symbol!");
            raise_an_exception();
            
            if(setjmp(buf)) {
                printf("Oooops, you seems to have typed an invalid operation! :(");
                return 1;
            }
            break;
    }
    // Checking if there is any decimal numbers behinb the decimal point!
    // 'fmod' here is being used as '%' in Python, same functionality as module.
    if (fmod(result, 1) == 0) {
        printf("%0.0lf", result);
    } else {
        printf("%lf", result);
    }
}

