#include "armstrong_numbers.h"
#include <stdio.h>
#include <math.h>

bool is_armstrong_number(int number){
    int sum = 0;
    int digits = 0;
    int temp = number;
    while (temp != 0){
        temp /= 10;
        digits++;
    }
    temp = number;
    while (temp != 0){
        sum += pow(temp % 10, digits);
        temp /= 10;
    }
    return sum == number;
}