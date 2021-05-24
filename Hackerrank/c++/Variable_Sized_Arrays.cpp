#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, q,r,c,s;
    cin >> n >> q;

    int *m[n];

    for(int i=0; i<n; i++){
        cin >> s;
        m[i] = new int[s];
        for(int j=0; j<s; j++){
            cin>>m[i][j];
        }          
    }

    for(int i=0; i<q; i++){
        cin >> r >> c;
        cout << m[r][c]<<endl;
    }
    
    return 0;
}

