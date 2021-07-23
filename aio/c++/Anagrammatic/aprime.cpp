#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("primes.in","r",stdin);
    freopen("primes.out","w",stdout);
    int p;
    cin>>p;
    vector<int> ap={2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 199, 311, 337, 373, 733, 919, 991};
    if(p>991){
        cout<<0<<endl;
        return 0;
    }
    else{
        for(int i=0;i<ap.size();i++){
            if(ap[i]>p){
                cout<<ap[i]<<endl;
                return 0;
            }
        }
    }
}