#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    int a;
    char skip;
    vector<int> v;
    stringstream s(str);
    
    while(s){
        if(s.peek() !=',')
        {   
            if(s >> a)
            {
            v.push_back(a);
            }
        }
        else{
            s >> skip;
        }
        
    }
    return v;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
