#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    int q;
    cin >> q;
    set <int> s;
    int x,y;
    while(q--)
    {
        cin >> x >> y;
        if(x==1)
        {
            s.insert(y);
        }
        else if(x==2)
        {
            s.erase(y);
        }
        else
        {
            if (s.find(y)==s.end())
            {
                cout << "No";
            }
            else{
                cout << "Yes";
            }
            cout<<endl;
        }
    }
    
    
    return 0;
    
}




