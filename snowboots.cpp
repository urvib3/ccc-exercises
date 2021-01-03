#include <iostream>
#include <fstream>
using namespace std;

int n, b, ans, f[250], s[250], d[250];
bool visited[250][250];

int main() {
  ifstream fin("snowboots.in");
  ofstream fout("snowboots.out");

  fin >> n >> b;
  for(int i=0; i<n; i++)
    fin >> f[i];
  for(int i=0; i<b; i++)
    fin >> s[i] >> d[i];

  for(int i=0; i<b; i++)
    for(int j=0; j<n; j++) {
        // tile has too much snow for boot
        if(s[i] < f[j]) { visited[j][i] = false; continue; }

        // initial state
        else if(i==0 && j==0) visited[j][i] = true;

        // possible from previous step from same boot
        for(int j2=0; j2<j; j2++)
          if(visited[j2][i] && j-j2 <= d[i]) visited[j][i] = true;

        // possible from boot change
        for(int i2=0; i2<i; i2++)
          if(visited[j][i2]) visited[j][i] = true;

        // reached the end
        if(visited[n-1][i]) {
            ans = i;
            cout << "b: " << b << endl;
            goto stop;
        }
    }
    stop:
    cout << "ans: " << ans;
    fout << ans << endl;

}
