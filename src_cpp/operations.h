#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

// function to add 2 numbers
void add()
{
    double num1, num2;
    cout << "Enter the 2 numbers :\n";
    cin >> num1 >> num2;

    cout << "Sum : " << num1 + num2;
}

// function to subtract 2 numbers
void sub()
{
    double num1, num2;
    cout << "Enter the 2 numbers :\n";
    cin >> num1 >> num2;

    cout << "Difference : " << num1 - num2;
}

// function to multiply 2 numbers
void mul()
{
    double num1, num2;
    cout << "Enter the 2 numbers :\n";
    cin >> num1 >> num2;

    cout << "Product : " << num1 * num2;
}

// funciton to divide 2 numbers and give the output in decimal
void div()
{
    double num1, num2;
    cout << "Enter the 2 numbers :\n";
    cin >> num1 >> num2;

    cout << "Division : " << num1 / num2;
}

// function to find percentage of a number
void percent()
{
    double num1, num2;
    cout << "Enter 2 number :\n";
    cin >> num1 >> num2;

    cout << num1 * num2 / 100;
}

// function to find factorial
long long unsigned int fact(int num1)
{
    long long unsigned int fac_res = 1;

    while (num1 > 1)
    {
        fac_res *= num1;
        num1 -= 1;
    }
    return fac_res;
}

// Function to find the number of permutations of n
// objects taking r at a time, that is nPr
long long unsigned int nPr(int num1, int num2)
{
    int temp;
    long long unsigned int nPr_res;

    if (num1 < num2)
    {
        temp = num1;
        num1 = num2;
        num2 = temp;
    }

    nPr_res = fact(num1) / fact(num1 - num2);
    return nPr_res;
}

// Function to find the number of combination of how n
// objects can be selected taking r at a time, that is nCr
void nCr()
{
    int num1, num2, temp;
    cout << "Enter 2 positive numbers :\n";
    cin >> num1 >> num2;

    if (num1 < num2)
    {
        temp = num1;
        num1 = num2;
        num2 = temp;
    }

    if (num1 == num2)
        cout << "nCr : " << 1;
    else
        cout << "nCr : " << nPr(num1, num2) / fact(num2);
}

// Function to do square of a number
void sqr()
{
    double num;
    cout << "Enter a number :\n";
    cin >> num;

    cout << num * num;
}

// Function to do cube of a number
void cube()
{
    double num;
    cout << "Enter a number : \n";
    cin >> num;

    cout << num * num * num;
}

// Function to get answer of number to the power n
void power()
{
    double num1, num2;
    cout << "Enter the number and its power :\n";
    cin >> num1 >> num2;

    cout << pow(num1, num2);
}

// Funciton to find sine of a given number
void sine()
{
    double num;
    cout << "Enter the number :\n";
    cin >> num;

    cout << sin(num);
}

// Funciton to find cosine of a given number
void cosine()
{
    double num;
    cout << "Enter the number :\n";
    cin >> num;

    cout << cos(num);
}

// Funciton to find tangent of a given number
void tangent()
{
    double num;
    cout << "Enter the number :\n";
    cin >> num;

    cout << tan(num);
}
