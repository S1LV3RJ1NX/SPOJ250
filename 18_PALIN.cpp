#include<bits/stdc++.h>
using namespace std;

int detect_nine(string s) {

    for(int i=0; i<s.length(); i++)
        if(s[i]!='9')
            return 0;
    return 1;
}

int main(){

    string s;
    int t;
    cin>>t;

    while(t--) {
        cin>>s;

        int i, j, num;
        // array of string len+3 for all 9's case
        char ans[s.length()+3];

        int n = s.length();

        // all nines in string
        if(detect_nine(s)) {
            ans[0] = '1';

            for(int i=1; i<n; i++)
                ans[i] = '0';
            ans[n] = '1';
            ans[n+1] = '\0';
            cout<< ans<<endl;
        } 
        else {
            //mid
            i = n/2;
            j=i;  // first of right

            // length is even
            if(n%2==0)
                i = i-1; // last of left

            //checking for equal from middle
            // <---i    j--->
            while (i>=0 && s[i]==s[j]) {
                i--;
                j++;
            }

            // not equal or string is palindrome
            if(i<0 || s[i] < s[j])
            {
                i = n/2;
                j = i;
                if (n%2==0)
                    i--;
                int carry = 1;

                while(i>=0) {
                    // convert that string to num
                    num = ((s[i]-'0')+carry);
                    // get 
                    carry = num/10;
                    s[i] = (num%10) + '0';

                    // copying reverse of it
                    s[j] = s[i];
                    i--;
                    j++;                    
                }
                
            }
            else{
                // copy reverse of it to second half
                while(i>=0) {
                    s[j] = s[i];
                    i--;
                    j++;
                }
            }
            cout<<s<<endl;
        }
    }

    return 0;
}