// https://www.spoj.com/problems/SAMER08F/
#include<iostream>

using namespace std;

int main() {
    int n;


    while (true) {
        cin>>n;
        if (n!=0) {
            cout<<((2*n+1)*(n+1)*n)/6<<endl;
        }
        else
            break;
    }

}
