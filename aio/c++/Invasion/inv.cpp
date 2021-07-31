#include <bits/stdc++.h>
using namespace std;
char a[1001][1001];
map<char,string> dic;
bool FIND(string s, char c){
    for(int i = 0; i<s.length(); i++){
        //cout<<c<<"  char  "<<s[i]<<"  s"<<endl;
        //if(s[0]=='g'){cout<<s<<" ggggg"<<endl;}
        if(s[i]==c){return false;}
    }
    //cout<<"true"<<endl;
    return true;
}
void chkr(int r,int c){
    //cout<<"startchkr"<<endl;
    for(int i=0;i<r;i++){
        for(int j=0;j<c-1;j++){
            //cout<<"startFIND"<<endl;
            //cout<<i<<"(i,j)"<<j<<endl;
            if(FIND(dic[a[i][j]],a[i][j+1])){
                dic[a[i][j]]+=a[i][j+1];
                //cout<<dic[a[i][j]]<<"  add"<<endl;
                dic[a[i][j+1]]+=a[i][j];
            }
        }
    }
    return;
}
void chkd(int r,int c){
    //cout<<"startchkd"<<endl;
    for(int i=0;i<r-1;i++){
        for(int j=0;j<c;j++){
            //cout<<"startFIND"<<endl;
            //cout<<i<<"(i,j)"<<j<<endl;
            if(FIND(dic[a[i][j]],a[i+1][j])){
                dic[a[i][j]]+=a[i+1][j];
                //cout<<dic[a[i][j]]<<"  add"<<endl;
                dic[a[i+1][j]]+=a[i][j];
            }
        }
    }
    return;
}

int main(){
    int r,c,ans=0;
    freopen("invin.txt","r",stdin);
    freopen("invout.txt","w",stdout);
    scanf("%d%d",&r,&c);
    for(char s='a';s<='z';s++){dic[s]=s;}
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cin>>a[i][j];
        }
    }
    chkr(r,c);
    chkd(r,c);
    for(pair<char,string> ele:dic){
        //cout<<ele.second<<endl;
        int length=ele.second.length();
        ans=max(ans,length);}
    cout<<ans-1<<endl;
}