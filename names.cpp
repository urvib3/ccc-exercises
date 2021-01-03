#include <iostream>
#include <fstream>
#include <set>
#include <bits/stdc++.h>
#include <vector>
using namespace std;

int N,G;
unordered_set<string> names;
unordered_set<string> ans;
vector<string> a;

int main() {
  ifstream fin("names.in");
  ofstream fout("names.out");
  
  fin >> N >> G;

  for(int i=0; i<N; i++) {
      string name;
      fin >> name;
      names.insert(name);
  }
  for(int i=0; i<G; i++) {
      string name;
      fin >> name;
      if(names.find(name) != names.end())
        ans.insert(name);
  }
  if(ans.size()) {
      unordered_set<string> :: iterator itr;
      for (itr = ans.begin(); itr != ans.end(); itr++)
          a.push_back(*itr);
      sort(a.begin(), a.end());
      for(int i=0; i<a.size(); i++)
        fout << a[i] << " ";
      return 0;
  }
  fout << -1;

}

