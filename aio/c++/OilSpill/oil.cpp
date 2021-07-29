#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("oilin.txt","r",stdin);
    freopen("oilout.txt","w",stdout);
    int r,c,k;
    cin>>r>>c>>k;
    char a[r][c];
    vector<pair<int,int>> cur;
    for (int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cin>>a[i][j];
            if (a[i][j]=='$'){
                cur.push_back(make_pair(i,j));
            }
        }
    }
    
    for(int i=0;i<k;i++){
        vector<pair<int,int>> newc;
        for(pair<int,int> ele:cur){
            if(ele.first>0 && a[ele.first-1][ele.second]=='.'){
                a[ele.first-1][ele.second]='*';
                newc.push_back(make_pair (ele.first-1, ele.second));
            }
            if(ele.second>0 && a[ele.first][ele.second-1]=='.'){
                a[ele.first][ele.second-1]='*';
                newc.push_back(make_pair (ele.first, ele.second-1));
            }
            if(ele.first<r-1 && a[ele.first+1][ele.second]=='.'){
                a[ele.first+1][ele.second]='*';
                newc.push_back(make_pair (ele.first+1, ele.second));
            }
            if(ele.second<c-1 && a[ele.first][ele.second+1]=='.'){
                a[ele.first][ele.second+1]='*';
                newc.push_back(make_pair (ele.first, ele.second+1));
            }
        }
        cur=newc;
    }
    for (int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cout<<a[i][j];
            if (j==c-1){
                cout<<"\n";
            }
        }
    }
    return 0;
}