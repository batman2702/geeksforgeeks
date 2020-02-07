#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int a[n];
	    for(int i=0;i<n;i++)
	    {
	        cin>>a[i];
	    }
	    for(int i=0;i<n;i++)
	    {
	        if(i==n-1)
	        {
	            if(a[i]==1)
	            {
	                cout<<0;
	            }
	            else
	            {
	                cout<<1;
	            }
	        }
	        else
	        {
	            if(a[i]==1)
	            {
	                cout<<0<<" ";
	            }
	            else{
	                cout<<1<<" ";
	            }
	        }
	    }
	    cout<<"\n";
	}
	return 0;
}
