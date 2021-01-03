#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
using namespace std;


int main() {
  ifstream fin("line.in");
  ofstream fout("line.out");

  int N, K;
  fin >> N >> K;

  for(int i=0; i<N; i++) {
      int current;
      fin >> current;
      if(K <= current) {
          fout << i;
          return 0;
      }
  }

}
