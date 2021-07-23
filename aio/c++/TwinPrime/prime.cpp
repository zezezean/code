#include<bits/stdc++.h>
#define inf 600000
using namespace std;

/*
int main(){
    freopen("primein.txt","r",stdin);
    freopen("primeout.txt","w",stdout);
    int n;
    cin>>n;
    bool A=true;
    vector<int> li={};
    cout<<2<<"\n";
    for(int i = 3; i<=n; i+=2){
        for(int j=0;j<li.size();j++){
            A=true;
            if(pow(li[j],2)>i){break;}
            if (i%li[j]==0){A=false;break;}
        }
        if (A){
            li.push_back(i);
            cout<<i<<"\n";
        }
    }
    return 0;
}
*/
int n;
bool a[inf+1];
long long num[inf+1]={1,1},prime[inf+1]={0},number=0;
void luojishai()                 
{
	//clock_t begin,end;                                             
	//begin=clock();
	for(int i=2;i<=n;++i) 
	{
		if(!num[i])
		  prime[number++]=i;
		for(int j=0;j<number && i*prime[j]<=n;j++)  
        {  
            num[i*prime[j]]=1;                 
            if(!(i%prime[j]))             
                break;
        }  
        if(num[i]==0){cout<<i<<"\n";}
    }
	//end=clock();
}

int main()
{
	freopen("primein.txt","r",stdin);
    freopen("primeout.txt","w",stdout);
	scanf("%d",&n);
	luojishai();
    return 0;   
}