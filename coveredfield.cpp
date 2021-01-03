#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;
#define maxx 100001
int* grid = new int[maxx*maxx];

int main() {
  ifstream fin("coveredfield.in");
  ofstream fout("coveredfield.out");
/*
  // all values of screws
  for(int i=0; i<maxx; i++)
    for(int j=0; j<maxx; j++)
      grid[i][j] = 0;

  int N, M;
  fin >> N >> M;
  cout << N << " " << M << endl;

  // ans[i] = # of screws w atleast i screws
  int ans[M+2];
  for(int i=0; i<=M+1; i++) ans[i] = 0;

  // initialize grid
  for(int i=0; i<N; i++) {
    //cout << " in first for loop" << endl;
    int x1, y1, x2, y2;
    fin >> x1 >> y1 >> x2 >> y2;
    //cout << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
    grid[x1][y1]++;
    grid[x1][y2+1]--;
    grid[x2+1][y1]--;
    grid[x2+1][y2+1]++;
  }
  
  // calculate all screws
  for(int i=0; i<maxx; i++)
    for(int j=0; j<maxx; j++) {
      if(i) grid[i][j] += grid[i-1][j];
      if(j) grid[i][j] += grid[i][j-1];
      if(i&&j) grid[i][j] -= grid[i-1][j-1];
      ans[grid[i][j]]++;
    }

  // calculate answers
  int c;
  for(int i=M; i; i--) {
    ans[i] += ans[i+1];
  }

  // print answers
  for(int i=1; i<=M; i++)
    fout << ans[i] << endl;

*/

}
