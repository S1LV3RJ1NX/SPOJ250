#include<bits/stdc++.h>

using namespace std;

map<int, long long> dp;

long long calculate_coins(int n) {
    if(n==0)
        return 0;
    if(dp[n]!=0)
        return dp[n];
    
    long long change = calculate_coins(n/2) + calculate_coins(n/3) + calculate_coins(n/4);

    if (change>n)
        dp[n] = change;
    else
        dp[n] = n;

    return dp[n];

}
int main(int argc, char const *argv[])
{
    int n;

    while(scanf("%d",&n)==1)
        printf("%lld\n",calculate_coins(n));

    return 0;
}
