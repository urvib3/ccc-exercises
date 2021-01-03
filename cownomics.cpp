#include <iostream>
#include <fstream>
using namespace std;

// "#"" = true, "."" = false
bool grid[1002][1002];
// id/component number of every #
int c[1002][1002];
int n, id, p[1000001], a[1000001];

void dfs(int i, int j) {
    if(j==262)
      cout << "i: " << i << " j: " << j;
    if(c[i][j]) return;
    c[i][j] = id;
    if(grid[i-1][j]) dfs(i-1,j);
    if(grid[i+1][j]) dfs(i+1,j);
    if(grid[i][j-1]) dfs(i,j-1);
    if(grid[i][j+1]) dfs(i,j+1);
}

// dfs(int i, int j)
  // if visited 
    // if(c[i][j]); means it already has id
      // return;
  // c[i][j] = id#
  // if there's a hashtag on the top
    // if(i && grid[i-1][j])
      // dfs(i-1, j)
  // if there's a hashtag on the bottom
    // if(n-i-1 && grid[i+1][j])
      // dfs(i+1,j)
  // if there's hastag on the left
    // if(j && grid[i][j-1])
      // dfs(i, j-1)
  // if there's hastag on right
    // if(n-j-1 && grid[i][j+1])
      // dfs(i, j+1)

void find_perimeters() {
  for(int i=1; i<=n; i++) {
    for(int j=1; j<=n; j++) {
        int r = c[i][j];
        p[r] += 4;
        if(grid[i-1][j]) p[r] -= 2;
        if(grid[i][j-1]) p[r] -= 2;
    }
  }
}
// perimeters
  // for i in n
    // for j in n
      // r = c[i][j]
      // perimeter[r] += 4
      // if hastag on top
        // if(i && grid[i-1][j])
          // perimeter[r] -= 2
      // if hastag on left 
        // if(j && grid[i][j-1])
          // perimeter[r] -= 2

int main() {
    ifstream fin("Untitled-1");
    ofstream fout("perimeter.out");

    fin >> n;
    //cout << "n: " << n;

    for(int i=0; i<n+2; i++) for(int j=0; j<n+2; j++) grid[i][j] = false;
    
    for(int i=1; i<=n; i++) for(int j=1; j<=n; j++) {
      char c;
      fin >> c;
      if(c == '#') grid[i][j] = true;
    }
    for(int i=1; i<=2; i++) for(int j=1; j<=2; j++)
      if((grid[i][j]) && (!c[i][j])) { id++; dfs(i,j);}
    //print out ids
    /*cout << "ids: " << endl;
    for(int i=0; i<n+2; i++) {
      for(int j=0; j<n+2; j++)
        cout << c[i][j] << " ";
      cout << endl;
    }*/

            /*
    find_perimeters();

    int besta=0, bestp=0;
    for(int i=1; i<=n; i++) for(int j=1; j<=n; j++)
        //cout << "i: " << i << " j: " << j << " c[i][j]: " << c[i][j] << " area of id: " << a[c[i][j]] << endl;
        a[c[i][j]] ++;
    // print areas
    //for(int i=0; i<=id; i++) cout << "i: " << i << " perimeter: " << p[i] << endl;
    for(int i=1; i<=id; i++) {
      //cout << "a[i]: " << a[i] << " besta: " << besta << " a[i] > besta: " << (a[i] > besta) << endl;
      if(a[i] > besta) { besta = a[i]; bestp = p[i];}
      else if(a[i] == besta) bestp = min(bestp, p[i]);
    }

    fout << besta << " " << bestp;
    */
}
// main
  // set all grid values to false
  // read in all values to grid
  // for i in n
    // for j in n
      // if character not already visited
        // if(!c[i][j])
          // id++
          // dfs(i,j)
  // perimeters
  // bestarea, bestperimeter
  // for i in n
    // for j in n
      // areas[c[i][j]]++
  // for every area calculated
  // for i in id (1:id+1)
    // if area[i] > bestarea 
      // update best a&p
    // if area[i] = bestarea
      // bestp = min(bestp, perimeter[id])

