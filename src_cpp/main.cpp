#include "interface.h"

// main function
int main()
{
    bool f = true;
    string cont = "y";
    // calling interface function to interact with the user
    while (f)
    {
        interface();
        cout << "\nDo you want to continue (y/n) : ";
        cin >> cont;
        f = (cont == "y") ? true : false;
    }

    cout << "Calculator closed!!\n";
    return 0;
}