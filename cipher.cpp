#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int main() {
  ifstream fin("cipher.in");
  ofstream fout("cipher.out");

  int N;
  fin >> N;

  int nums[N];
  for(int i=0; i<N; i++)
    fin >> nums[i];

  string letters = " abcdefghijklmnopqrstuvwxyz";

  int n = sizeof(nums) / sizeof(nums[0]);
  reverse(nums, nums + n);

  for(int i=0; i<N; i++) {
    int c = nums[i];
    if(c == -1) fout << " ";
    else fout << letters.at(nums[i]);
  }
}
