#include <iostream>
using namespace std;
int main(){
    freopen("ninjain.txt","r",stdin);
    freopen("ninjaout.txt","w",stdout);
    int n,k,ans;
    cin>>n>>k;
    ans=max(0,n-((n-1)/(k+1)+1));
    cout<<ans<<endl;
}