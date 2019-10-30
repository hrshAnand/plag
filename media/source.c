#include <stdio.h>

// IIT se hain BC!  //

int main()
{
	// ios_base::sync_with_stdio(false); 
 //    cin.tie(NULL); 
	int n;
	while(n--);
	
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

    	
	return 0;
}