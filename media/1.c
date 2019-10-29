#include<stdio.h>
#define ll long long
#define l int
			else if(arr[i][0]==arr[j][0]){
				if(arr[i][1]<arr[j][1]){
					temp=arr[i][1];
					arr[i][1]=arr[j][1];
					arr[j][1]=temp;
				}
			}


// int lis(int arr[][2],int n){
// 	int out[n];
// 	out[0]=1;
// 	int maxi=0;
// 	for (int i = 0; i < n-1; ++i)
// 	{
// 		int tmax=1;
// 		for (int j = 0; j <= i; ++j)
// 			if(arr[i+1][1]>=arr[j][1])
// 				tmax=out[j]+1>tmax?out[j]+1:tmax;
// 		out[i+1]=tmax;
// 		maxi=out[i+1]>maxi?out[i+1]:maxi;
// 	}
// 	return maxi;
// }


int lis( int arr[][2], int n )  
{  
    int lis[n]; 
   
    lis[0] = 1;    
  
    for (int i = 1; i < n; i++ )  
    { 
        lis[i] = 1; 
        for (int j = 0; j < i; j++ )   
            if ( arr[i][1] >= arr[j][1] && lis[i] < lis[j] + 1)  
                lis[i] = lis[j] + 1;  
    } 
  
    int maxi=lis[0];
    for (int i = 0; i < n; ++i) if(lis[i]>maxi) maxi=lis[i];
    return maxi;
}  

int main(){
	int t,n;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		int arr[n][2];
		for (int i = 0; i < n; ++i) scanf("%d",&arr[i][0]);
		for (int i = 0; i < n; ++i) scanf("%d",&arr[i][1]);
		s(arr,n);
		printf("%d\n",lis(arr,n));
	}
	return 0;
}