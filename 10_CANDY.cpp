/*
The candies can only be divided equally, if, the sum of candies is divisible by number of students.
Then the total number of operations required would be equal to the operations required in making the 
contents of the packets equal to the ‘mean’.
*/
#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{       
    /* code */
    int t;
    cin>>t;
    while(t!=-1) {
        int ans= 0, mean=0, sum=0, arr[t];

        
        for(int i = 0; i < t; i++)
        {
            cin>>arr[i];
            sum+=arr[i];
        }

        mean = sum/t;

        if (mean*t == sum) {
            
            for(int i = 0; i < t; i++)
            {
                if (mean>arr[i]) {
                    ans+= mean-arr[i];
                }
            }
            cout<<ans<<endl;
        }
        else
            cout<<"-1"<<endl;
        cin>>t;
        
    }
    return 0;
}
