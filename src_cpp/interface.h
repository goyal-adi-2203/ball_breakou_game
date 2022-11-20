#include "operations.h"

void check_op(string op);

// output function to do operations and show on the terminal
void interface()
{

    // string object op to input the operation
    string op;
    cout << "Enter the operation you want to perform : \n";
    cin >> op;

    // calling function check
    check_op(op);
}

// function to check the operation entered by the user
void check_op(string op)
{

    // checking if operation is addition
    if (op == "add")
        add();
    // checking if operation is subtraction
    else if (op == "sub")
        sub();
    // checking if operation is multiply
    else if (op == "mul")
        mul();
    // checking if operation is division
    else if (op == "div")
        div();
    // cheking if operation to find percentage
    else if (op == "percent")
        percent();
    // checking if operation is factorial
    else if (op == "fact")
    {
        int num1;
        long long unsigned int fac_res;
        cout << "Enter 1 positive integer to find factorial :\n";
        cin >> num1;
        fac_res = fact(num1);
        cout << fac_res;
    }
    // checking if operation is nPr
    else if (op == "nPr")
    {
        int num1, num2;
        long long unsigned int nPr_res;
        cout << "Enter 2 positive numbers :\n";
        cin >> num1 >> num2;
        nPr_res = nPr(num1, num2);
        cout << nPr_res;
    }
    // checking if operation is nCr
    else if (op == "nCr")
        nCr();
    // checking if operation is finding square
    else if (op == "sqr")
        sqr();
    // checking if operation is to find cube
    else if (op == "cube")
        cube();
    // checking if operation is to find n^k
    else if (op == "pow")
        power();
    // checking if operation is sine
    else if (op == "sin")
        sine();
    // checking if operation is sine
    else if (op == "cos")
        cosine();
    // checking if operation is sine
    else if (op == "tan")
        tangent();
    else
        cout << "SORRY!! I can't do this.\n";
}