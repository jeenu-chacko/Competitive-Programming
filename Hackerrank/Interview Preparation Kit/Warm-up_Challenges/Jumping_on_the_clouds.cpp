
#include <bits/stdc++.h>

using namespace std;

int main()
{   
    vector <int> v;
    int i,n,x,count=0;
    cin>>n;
    v.reserve(n);
    for( i=0;i<n;i++)
    {
        cin>>x;
        v.push_back(x);
    }
    i=0;
    
    while(i<n-1)
    {
        if(v[i+2]==0 && i+2<n)
        {
            i=i+2;
        }
        else
        {
            i=i+1;
        }
        count=count+1;
       
    }
    cout<<count;
    
    return 0;
}
