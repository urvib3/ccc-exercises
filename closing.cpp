#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

vector<int> barn[3000];
int closings[3000];
bool open[3000];
bool visited[3000];
bool connected[3000];
int reached;
int N, M;

void dfs(int c) {
  //cout << "c: " << c << " open? " << open[c] << endl;
  if(visited[c] || (!open[c])) return;
  visited[c] = true;
  reached++;
  for(int i=0; i<barn[c].size(); i++) {
    dfs(barn[c][i]);
  }
}

int main() {
  ifstream fin("closing.in");
  ofstream fout("closing.out");
  fin >> N >> M;

  int a,b;
  for(int i=0; i<M; i++) {
    fin >> a >> b;
    barn[a].push_back(b);
    barn[b].push_back(a);
  }
  for(int i=0; i<N; i++)
    fin >> closings[i];

  int c;
  int n = N;
  while(n--) {
    //cout << "N: " << N << " n: " << n << endl;
    c = closings[n];
    open[c] = true;
    dfs(c);
    if(reached == N-n) connected[n] = true;
    //cout << "current house: " << c << "  connected: " << connected[n] << " reached: " << reached << " required: " << N-n << endl;
    reached = 0;
    for(int i=0; i<3000; i++) visited[i] = false;
  }
  for(int i=0; i<N; i++) {
    if(connected[i]) fout << "YES" << endl;
    else fout << "NO" << endl;
  }

}


//dfs(c)
  // if(visited[c] || !open[c]) return
  // visited[c] = true
  // reached++
  // for i in c's vector size
    // dfs(vector's[i])

// vector<int> barn[3000]
// bool open[3000]
// bool visited[3000]
// bool connected[3000]
// int reached
// int N, M
// for i in M
  // int a,b
  // barn[a].push_back(b) & vice versa
// int n
// while(n--)
  // int c
  // open c
  // dfs(c)
  // if(reached == N-n)
    // connected[N-n] = true
  // reached = 0
  // for element in visited: set to false
// for i in connected: print out true or false
