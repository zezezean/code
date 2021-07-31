#include <iostream>
using namespace std;
int main(){
    freopen("wetin.txt","r",stdin);
    freopen("wetout.txt","w",stdout);
    int x,tot=0;
    for(int i=0;i<8;i++){
        cin>>x;
        tot=max(0,tot+x-10);
    }
    cout<<tot<<endl;
}