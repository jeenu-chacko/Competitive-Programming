#include <bits/stdc++.h>

using namespace std;

void sales(vector <int> v)
{
    unordered_map<int, int> s;
    for (int i = 0; i < v.size(); i++) 
        s[v[i]]++;
          
    int count=0;
    for(auto a:s)
    {
        if(a.second%2==0)
        {
            count=count+(a.second/2);
        }
        else{
            count=count+((a.second-1)/2);
        }
    }
    cout<<count;
}

int main()
{
    int n;
    vector<int> v;
    cin >> n;
    
    for(int i=0;i<n;i++)
    {
        int x;
        cin >> x;
        v.push_back(x);
    }
    sales(v);
    return 0;
}

