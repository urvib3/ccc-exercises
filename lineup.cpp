#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <stdio.h>
using namespace std;

int translator(string cow){
  string coworder[] = {"Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"};
  for(int i=0; i<8; i++){
    if(coworder[i] == cow)
      return i;
  }
  return -1;
}
int main() {
    ifstream fin("lineup.in");
    ofstream fout("lineup.out");
    int n;
    fin >> n;
    vector<int> next_to[8];
    set<int> processed;
    int order[8];

    // initialize arrays with all cows next to ith cow in next_to1/2 arrays
    for(int i=0; i<8; i++) {
      order[i] = -1;
    }
    for(int i=0; i<n; i++){
      string first, second;
      for(int j=0; j<6; j++){
          string word;
          fin >> word;
          //cout << word;
          if(j==0) first = word;
          if(j==5) second = word;
      }
      int cow1 = translator(first);
      int cow2 = translator(second);
      next_to[cow1].push_back(cow2);
      next_to[cow2].push_back(cow1);
    }
    int index_in_order = 0;
    for(int i=0; i<8; i++){
        int first;
        for(int j=i; j<8; j++) {
          if(next_to[j].size() <= 1 && processed.count(j) == 0) {
            first = j;
            processed.insert(first);
            break;
          }
        }
        order[index_in_order] = first;
        //fout << "first: " << order[i];
        index_in_order++;
        while(next_to[first].size() == 1){
          int second = next_to[first].at(0);
          processed.insert(second);
          order[index_in_order] = second;
          int index=0;
          if(next_to[second].size() == 2){
              int keep;
              if(next_to[second].at(0) == first)
                keep = next_to[second].at(1);
              else
                keep = next_to[second].at(0);
              next_to[second].clear();
              next_to[second].push_back(keep);
          }
          else
            next_to[second].clear();
          index_in_order ++;
          first = second;
        }
        if(order[7] != -1) break;
        
    }
    string coworder[] = {"Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"};
    for(int i=0; i<8; i++)
        fout <<  coworder[order[i]] << "\n";
}
    


