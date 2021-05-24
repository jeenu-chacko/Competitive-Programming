#include <bits/stdc++.h> 
using namespace std; 


int main()
{
    int n,count=0,valley=0;
    string s;
    cin>>n;
    cin>>s;
    for(int i=0;i<s.length();i++)
    {
        if(s[i]=='D')
        {
            if(count==0)
            {
            valley+=1;
            count=count-1;
            }
            else{
                count=count-1;
            }
        }
        else{
            count=count+1;
        }
    }
    cout<<valley;
    
    return 0;  
}
