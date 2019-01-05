// https://www.spoj.com/problems/TOANDFRO/

#include<iostream>
#include<string>

using namespace std;

int main(){

    int col, rows;
    string msg;

    while(true) {
        cin >> col;

        if (col == 0)
            break;
        else{

            cin>>msg;
            rows = msg.length() / col;
            // cout<<rows<<endl;
            int k = 0;
            char s[rows][col];
            int a; 

            // look how rows are written
            for(int i=0; i<rows; i++)
            {
                if(i%2){
                    for(int j=col-1; j>=0; j--)
                        s[i][j] = msg[k++];
                }
                else{
                    for(int j=0; j<col; j++ )
                        s[i][j] = msg[k++];
                }
            }
                
            for(int j=0; j<col; j++)
                for(int i=0; i<rows; i++ ){
                    cout<<s[i][j];
                    
                }
            cout<<endl;
                    


        }
    }

    return 0;
}