#include <iostream>
#include <fstream>
using namespace std;

int screws[1000][1000];
int visited[1000][1000];
int maxx;
int current;
int N, M;

void dfs(int i, int j) {
  if(i < 0 || j < 0 || i >= N || j >= M || !screws[i][j] || visited[i][j]) {
    if(current > maxx) maxx = current;
    return;
  }

  //cout << "cur1: " << current << endl;
  current++;
  //cout << "cur2: " << current << endl;
  visited[i][j] = true;
  //cout << "i: " << i << " j: " << j << " current: " << current << " max: " << maxx << endl;

  dfs(i, j-1);
  dfs(i, j+1);
  dfs(i-1, j);
  dfs(i+1, j);
}

int main() {
  ifstream fin("islands.in");
  ofstream fout("islands.out");

  fin >> N >> M;

  // initialize screws
  for(int i=0; i<N; i++) {
    for(int j=0; j<M; j++) {
        fin >> screws[i][j];
        //cout << screws[i][j] << " ";
        visited[i][j] = false;
    }
    //cout << endl;
  }

  // dfs on every island
  for(int i=0; i<N; i++)
    for(int j=0; j<M; j++) {
      current = 0;
      dfs(i, j);
    }

  fout<<maxx;
  
}
