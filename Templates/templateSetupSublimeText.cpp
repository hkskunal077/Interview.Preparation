// If you are using Sublime Text then follow these steps to get a template:

// open sublime and go to tools>developer>new snippet and click on it
// replace the existing code with the code written below and save it with some name.

#include<bits/stdc++.h> 
using namespace std; 
#define n '/n'
void solve(); 
int main() 
{ 
ios_base::sync_with_stdio(false);cin.tie(NULL); 

#ifndef ONLINE_JUDGE 
freopen("input.txt", "r", stdin); 
freopen("error.txt", "w", stderr); 
freopen("output.txt", "w", stdout); 
#endif 

int t=1; 
${2:/*is Single Test case?*/}cin>>t; 
while(t--) 
{ 
	solve(); 
	cout<<"\n"; 
} 

cerr<<"time taken : "<<(float)clock()/CLOCKS_PER_SEC<<" secs"<<endl; 
return 0; 
} 
void solve() 
{ 
} 



