#include <iostream>
#include <fstream>
#include <algorithm>
#define max_x 100000
using namespace std;

int x[max_x], y[max_x];
int pos[max_x], neg[max_x];
int mid[max_x];

bool cmp(int a, int b) {
  if(neg[a] == neg[b])
    return pos[a] > pos[b];
  return neg[a] < neg[b];
}

int main() {
    ifstream fin("mountains.in");
    ofstream fout("mountains.out");
    int n;
    fin >> n;
    for(int i=0; i<n; i++) {
      fin >> x[i] >> y[i];
      pos[i] = x[i] + y[i];
      neg[i] = x[i] - y[i];
      mid[i] = i;
    }
    sort(mid, mid+n, cmp);
    int visible = 0;
    int maxpos = 0;
    for(int i=0; i<n; i++) {
        if(pos[mid[i]] > maxpos) {
            visible++;
            maxpos = pos[mid[i]];
        }
    }
    fout << visible;
}
