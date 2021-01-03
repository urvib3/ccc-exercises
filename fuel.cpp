#include <iostream>
#include <fstream>
using namespace std;

int main() {
  ifstream fin("fuel.in");
  ofstream fout("fuel.out");

  int N, K;
  fin >> N >> K;

  int fuels[N];
  for(int i=0; i<N; i++)
    fin >> fuels[i];
  int refills[N+1];

  for(int i=0; i<=N; i++) refills[i] = 0;

  for(int i=0; i<K; i++) {
    int s, e, v, f;
    fin >> s >> e >> v >> f;
    int increase = v * f;
    s--; e--;
    cout << "increase: " << increase << endl;;
    refills[s] += increase;
    refills[e+1] -= increase;
  }
  

  int c = 0;
  for(int i=0; i<N; i++) {
    c += refills[i];
    fout << fuels[i] + c << endl;
  }
}
