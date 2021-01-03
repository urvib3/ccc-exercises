#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
int ids[1000000];
int placesums[] = {1, 1, 2, 6, 24, 120, 720, 5040};

void permute(string a, int index, int l, int r) {
  // Base case
  long sum=0;
  if (l == r) {
    for(int i=0; i<=r; i++) {
      sum += (pow(10, (r - i)) * (a.at(i)-96));
    }
    ids[index]+=sum;
  } else {
    for (int i=l; i<=r; i++) {
      swap(a[l], a[i]);
      permute(a, index, l+1, r);
      swap(a[l], a[i]);
    }
  }
}

int calculate(string a) {
    int size = a.size();
    int nums[size];
    for(int i=0; i<size; i++){
        nums[i] = a.at(i) - 96;
    }
    long sum = 0;
    int placesum;
    for(int i=0; i<size; i++) {
      placesum += (placesums[size-1])*nums[i];
    }
    // cout << "placesum: " << placesum << endl;
    int carry = 0;
    for(int i=0; i<size; i++) {
      int current = placesum+carry;
      if(i == size-1) {
        sum += pow(10, size-1) * current;
      }
      else if(current-9) {
        sum += pow(10, i) * (current%10);
        carry = (current - current%10) / 10;
      } else {
        sum += current;
        carry = 0;
      }
      //cout << "current: " << current << " currentsum: " << sum << endl;
    }
    return sum;
}


int main() {
  ifstream fin("favorite.in");
  ofstream fout("favorite.out");
  
  int N;
  fin >> N;

  for (int i=0; i<N; i++){
    string a;
    fin >> a;
    //permute(a, i, 0, a.size()-1);
    //fout << ids[i] << endl;
    int id = calculate(a);
    fout << id << endl;
  }
}


