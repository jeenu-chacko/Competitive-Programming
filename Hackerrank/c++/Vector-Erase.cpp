#include <bits/stdc++.h> 
using namespace std;


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    unsigned int x,z,a,b,y;
    vector <int> v;
    cin >> x;
    
    while(x--)
    {
        cin >> y;
        v.push_back(y);
    }
    
    cin >> z;
    v.erase(v.begin()+(--z));
    
    cin >> a >> b;
    
    v.erase(v.begin()+(--a),v.begin()+(--b));
    
    cout << v.size() << endl;
    
    for (auto i:v)
    {
        cout << i << " "; 
    }
    
    return 0;
}

