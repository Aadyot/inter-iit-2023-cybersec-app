#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    ifstream is("treasure");
    ofstream os("treasure.txt");

    vector<unsigned char> v;

    while(!is.eof()){
        unsigned char c;
        is>>c;
        v.push_back(c);
    }

    for(auto c : v){
        //if(c<32 || c>=127) continue;
        os<<c;
    }
}