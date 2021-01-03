#include <iostream>
#include <fstream>
using namespace std;

int main() {
  ifstream fin("game.in");
  ofstream fout("game.out");

  int N;
  fin >> N;

  int seats[N], steps[N+1];
  bool gone[N+1];
  for(int i=1; i<=N; i++) gone[i] = false;

  for(int i=1; i<=N; i++) fin >> steps[i];

  for(int i=1; i<=N; i++) seats[i-1] = i;
  for(int i=0; i<N; i++) cout << seats[i] << endl;

  // current position of intern
  int currpos=0;
  int currintern = 1;
  int ans;
  /*
  while(true) {
      if(gone[currintern]) {ans = currintern; cout << "intern " << currintern << " is repeated" << endl;break; }
      seats[currpos] = 0;
      int original = currintern;
      cout << endl << "seats: ";
      for(int i=0; i<N; i++) cout << seats[i] << " ";
      cout << endl;
      gone[currintern] = true;
      cout << "original seats: ";
      for(int i=0; i<N; i++) cout << seats[i] << " ";
      cout << endl;
      cout << "after seats: ";
      for(int i=0; i<N; i++) cout << seats[i] << " ";
      cout << endl;
      // seats have someone in arrived, now current,  position, fix intern
      cout << "intern in arrived chair: " << seats[currpos] << endl;
      if(seats[currpos]) {currintern = seats[currpos];}
      else {ans = currintern; cout << "intern " << currintern << " in empty chair" << endl; break;}
      cout << "original: " << original << " currintern: " << currintern << endl;
      seats[currpos] = original;
      int currsteps = steps[currintern];
      cout << "original currpos: " << currpos << " currsteps: " << currsteps;
      currpos+= currsteps;
      currpos = currpos%N;
      cout << "current intern: " << currintern << "current steps: " << currsteps << "current position: " << currpos << endl;
  }
  */
  int originalintern = 1;
  int first = 0;
  while(true) {
      cout << endl << "seats: ";
      for(int i=0; i<N; i++) cout << seats[i] << " ";
      cout << endl;

      // if currintern is empty, then return
      if(currintern==0) {ans = originalintern; cout << "intern " << originalintern << " in empty chair"; break;}

      // initialize current intern to that in current pos
      cout << "currintern: " << currintern << endl;
      currintern = originalintern;

      // if it's the first intern, make its seat empty
      if(first == 0) seats[0] = 0;

      // check if current intern has already gone
      if(gone[currintern]) {ans = currintern; cout << "intern " << currintern << " is repeated" << endl;break; }

      // update currpos
      int currsteps = steps[currintern];
      currpos+= currsteps;
      currpos = currpos%N;
      originalintern = seats[currpos];
      seats[currpos] = currintern;
      first++;
  }


  fout << ans << endl;
}
