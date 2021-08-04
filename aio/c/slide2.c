#include<stdio.h>
#include<string.h>

int main(void){
    int n,a,b,c,arr[15][15]={0},t=7,game=0;
    printf("How many blocks? ");
    scanf("%d",&n);
    printf("Enter blocks: \n");
    for (int i=0;i<n;i++){
        scanf("%d%d%d",&a,&b,&c);
        arr[a][b]=1;
    }
    for(int i=0;i<15;i++){
        if(i==t){printf("> ");}
        else{printf("  ");}
        for(int j=0;j<15;j++){
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    while(1){
	    int com,comt=0;
	    scanf("%d",&com);
	    switch(com){
	        case 1: 
	        scanf("%d",&comt);
	        switch(comt){
	            case 1:
	            t-=1;break;
	            case -1:
	            t+=1;break;
	            default:break;
	        }break;
	        case 2:
	        for(int i=0;i<15;i++){
                if(arr[t][i]==1){n-=1;}
	        	arr[t][i]=0;
                if(n==0){game=1;break;}
	        }break;
            case 3:
            for(int i=0;i<15;i++){
	        	if(arr[i][0]==1){game=-1;break;}
            }
            if (game!=-1){
                for(int i=0;i<14;i++){
                    arr[t][i]=arr[t][i+1];
                }
            }break;
	    }
	    printf("\n");
	    for(int i=0;i<15;i++){
	        if(i==t){printf("> ");}
	        else{printf("  ");}
	        for(int j=0;j<15;j++){
	            printf("%d ",arr[i][j]);
	        }
	        printf("\n");
	    }
        switch(game){
            case -1: 
            printf("Game Lost!\n"); return 0;
            case 1: 
            printf("Game Won!\n"); return 0; 
            default:break;
        }
    }
}