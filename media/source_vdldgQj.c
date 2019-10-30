#include<stdio.h>
int cmax(int* arr,int j,int k){
	//printf("Hello\n");
	int out=0;
	for (int i = j; i < j+k; ++i){
		//printf("%d\n",arr[i]);
		if(arr[i]>out)
			out=arr[i];
	}
	return out;
}
int main(){
	int n,k;
	scanf("%d",&n);
	//printf("%d\n",n);
	int arr[n];
	for (int i = 0; i < n; ++i){scanf("%d",&k); arr[i]=k;}
	scanf("%d",&k);
	//for (int i = 0; i < n; ++i)printf("%d\n",arr[i]);
	int maxi=cmax(arr,0,k);
	printf("%d ",maxi);
	for (int i = 1; i < n-k+1; ++i)
	{
		if(arr[i]>maxi)
			maxi=arr[i];
		else{
			maxi=cmax(arr,i,k);
		}
		printf("%d ",maxi);
	}
	printf("\n");
	
}