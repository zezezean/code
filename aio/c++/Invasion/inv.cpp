#include <bits/stdc++.h>
using namespace std;
char a[1001][1001];
map<char,string> dic;
void chkr(int r,int c){
    for(int i=0;i<r;i++){
        for(int j=0;j<c-1;j++){
            if(dic[a[i][j]].find(a[i][j+1])==dic[a[i][j]].end()){
                dic[a[i][j]]+=a[i][j+1];
                dic[a[i][j+1]]+=a[i][j];
            }
        }
    }
    cout<<"r1"<<endl;
    return;
}
void chkd(int r,int c){
    for(int i=0;i<r-1;i++){
        for(int j=0;j<c;j++){
            if(dic[a[i][j]].count(a[i+1][j])==0){
                dic[a[i][j]]+=a[i+1][j];
                dic[a[i+1][j]]+=a[i][j];
            }
        }
    }
    cout<<"r2"<<endl;
    return;
}

int main(){
    int r,c,ans=0;
    scanf("%d%d",&r,&c);
    for(char s='a';s<='z';s++){dic[s]=s;}
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cin>>a[i][j];
        }
    }
    chkr(0,0);
    chkd(0,0);
    for(pair<char,string> ele:dic){
        int length=ele.second.length();
        ans=max(ans,length);}
    cout<<ans<<endl;
}