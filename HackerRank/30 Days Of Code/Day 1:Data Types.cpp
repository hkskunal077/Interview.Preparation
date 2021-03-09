#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";


    
    // Declare second integer, double, and String variables.
    int sint;
    double sdouble;
    string sstring;
    
    // Read and save an integer, double, and String to your variables.
    cin>> sint;
    cin>>sdouble;
    cin.ignore();
    getline(cin, sstring);
    
    

    // Note: If you have trouble reading the entire string, please go back and review the Tutorial closely.
    
    // Print the sum of both integer variables on a new line.
    int nsum = sint + i;
    cout<<nsum<<"\n";
        
    
    // Print the sum of the double variables on a new line.
    double nsumd = sdouble +d;
    cout<<setprecision(1)<<fixed<<nsumd<<"\n";

    
    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    string nsums  = s + sstring;
    cout<< nsums;
    return 0;
}
