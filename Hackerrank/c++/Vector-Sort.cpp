#include <bits/stdc++.h> 
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<int> v;
    
    unsigned int n,x;
    cin >> n;
    v.reserve(n);
    while(n--)
    {
        cin >> x;
        v.push_back(x);
    }    
    sort(v.begin(),v.end());
    
    for(auto y:v)
    {
        cout << y <<" ";
    }
    
        
    return 0;
}

