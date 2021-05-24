#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <algorithm>
using namespace std;


int main() {
    map<string,int> m;
    int q,type,Y;
    string X;
    cin >>q;
    while(q--)
    {
        cin >> type >> X;
        
        if(type==1)
        {
            cin>>Y;
            m[X] +=Y;
        }
        else if(type == 2)
        {
            m.erase(X);
        }
        else{
            if(m.find(X)!=m.end())
            {
                cout<< m[X] << endl;
            }
            else{
                cout<<'0'<< endl;
            }
        }
        
    }

    return 0;
}




