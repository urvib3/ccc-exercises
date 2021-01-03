#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
using namespace std;


int main() {
  ifstream fin("grandprix.in");
  ofstream fout("grandprix.out");

  int N, P;
  fin >> N >> P;

  int powers[N];
  for(int i=0; i<N; i++)
    fin >> powers[i];

  for(int i=0; i<N; i++)
    for(int j=i; j<N; j++)
      if(powers[i]+powers[j] == P) {
          fout << i+1 << " " << j+1;
          return 0;
      }

}
