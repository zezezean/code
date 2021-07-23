#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);cout.tie(0);
    freopen("spiesin.txt","r",stdin);
    freopen("spiesout.txt","w",stdout);
    int s1,s2,start=-1,temp,ans=0;
    bool b1=false,b2=false;
    cin>>s1;
    int a1[s1*2];
    for(int i=0;i<s1*2;i+=2){
        cin>>a1[i]>>a1[i+1];
    }
    cin>>s2;
    int a2[s2*2];
    for (int i=0;i<s2*2;i+=2){
        cin>>a2[i]>>a2[i+1];
    }
    int i=0,j=0;
    while(i<s1*2 and j<s2*2){
        if(a1[i]<=a2[j]){
            if(i%2==0){b1=true;}
            else{b1=false;}
            temp=a1[i];
            i++;
            //cout<<i<<" "<<a1[i-1]<<" "<<"a1"<<endl;
        }
        else{
            if(j%2==0){b2=true;}
            else{b2=false;}
            temp=a2[j];
            j++;
            //cout<<j<<" "<<a2[j-1]<<" "<<"a2"<<endl;
        }
        //cout<<b1<<b2<<endl;
        if(b1==true && b2==true){
            start=temp;
            //cout<<start<<" "<<"start"<<endl;
        }
        else if(start!=-1){
            ans+=temp-start;
            //cout<<temp<<" "<<"temp"<<endl;
            start=-1;
        }
    }
    cout<<ans<<endl;
    return 0;
}