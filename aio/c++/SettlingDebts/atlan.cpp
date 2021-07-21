#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);cout.tie(0);
    freopen("debtsin.txt","r",stdin);
    freopen("debtsout.txt","w",stdout);
    int n;
    cin>>n;
    int arr[n];
    int ans=-1;
    //bool eddie=false;
    for(int i = 0;i<n;i++){
        cin>>arr[i];
    }
   // cout<<0<<endl;
    for(int i = 0;i<n;i++){
        //cout<<"a"+to_string(i)<<endl;
        int tot=0,leng=0;
        for(int j=i;j<2*n;j++){
            //cout<<"b"+to_string(j)<<endl;
            tot+=arr[j%n];
            //cout<<arr[j%n]<<endl;
            //cout<<"t"+to_string(temp)<<endl;
            leng++;
            if(tot>0){i=j;break;}
            if (leng==n){
                ans=i+1;
                cout<<ans<<endl;
                //fclose(stdout);
                return 0;
            }
        }
    }
}