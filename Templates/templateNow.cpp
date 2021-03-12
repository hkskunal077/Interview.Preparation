//Number 1 setup requirement is the FAST I/O operations
//we will try to achieve the same output speed using
//cout/cin as printf/scanf by FAST I/O
#include <bits/stdc++.h>
using namespace std;
#define nn '\n'
#define ll long long int

//stack, vector, queue, etc STL
//We will use them when it will be needded

void fastscan(int &number)
{
	//variable to indicate sign of input number
	bool negative = false;
	register int c;

	number = 0;

	//extract current character from buffer
	c = getchar();
	if (c=='-'){
		negative = true;
		c = getchar();
	}

	for (; (c>47 && c< 58); c=getchar())
		number = number*10 + c -48;

	if (negative)
		number *= -1;
}


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif


    int number; fastscan(number);
    cout<<number;

    return 0;
}
