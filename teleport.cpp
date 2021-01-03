#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
using namespace std;


int main() {
  ifstream fin("teleport.in");
  ofstream fout("teleport.out");
  int n;
  map<int,int> slopes;
  fin >> n;
  long long curr_f = 0;
  for(int i=0; i<n; i++) {
    int a,b;
    fin >> a >> b;
    curr_f += abs(a-b);

    if(abs(a) > abs(a-b)) continue;
    slopes[b]+=2;
    if(a<0 && a < b) {slopes[0]--; slopes[2*b]--;}
    if(a>=0 && a>=b) {slopes[0]--; slopes[2*b]--;}
    if(a<0 && a>=b) {slopes[2*a]--; slopes[2*b-2*a]--;}
    if(a>=0 && a<b) {slopes[2*a]--; slopes[2*b-2*a]--;}
  }
  long long slope = 0, min_f = curr_f, curr_y = -2000000000;
  for(auto p: slopes) {
    int new_y = p.first;
    curr_f += slope * (new_y-curr_y);
    slope += p.second;
    curr_y = new_y;
    min_f = min(min_f, curr_f);
  }
  fout << to_string(min_f) ;
}
