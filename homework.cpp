#include <iostream>
#include <fstream>
#include <stack>
using namespace std;

int main() {
  ifstream fin("homework.in");
  ofstream fout("homework.out");
  
  int n;
  fin >> n;

  double scores[n];

  for(int i=0; i<n; i++)
    fin >> scores[i];

  double minscore = min(scores[n-1], scores[n-2]), total = scores[n-1] + scores[n-2], maxaverage = max(scores[n-1], scores[n-2]);
  stack<int> maxes;
  maxes.push(n-2);
  //cout << "initial minscore: " << minscore << endl;
  //cout << "inital maxaverage: " << maxaverage << endl;
  //cout << "initial total: " << total << endl;
  //cout << "initial score: " << scores[n-1] << endl;

  for(int i=n-3; i>=1; i--) {
    //cout << "minscore: " << minscore << endl;
    double cur = scores[i];
    total += cur;
    //cout << "cur: " << cur << endl;
    minscore = min(minscore, cur);
    //cout << "n-i: " << n-i << endl;
    double curaverage = (total-minscore)/(n-i-1);
    //cout << "total: " << total << " curaverage: " << curaverage << endl;
    if(curaverage>maxaverage) {
        maxes = {};
        maxes.push(i);
        maxaverage = curaverage;
    }
    else if(curaverage==maxaverage)
      maxes.push(i);
  }

  while(!maxes.empty()) {
    fout << maxes.top() << endl;
    maxes.pop();
  }
}
