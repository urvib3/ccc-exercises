#include <stdio.h>

int solve(int k) {
  int x;
  scanf("%d", &x);
  int lmeters = 0;
  int rmeters = 0;
  int secs = 0;
  for(int curspeed = 1;; curspeed++) {
      lmeters += curspeed;
      secs++;;
      if(lmeters+rmeters >= k) return secs;
      if(curspeed >= x) {
          rmeters += curspeed;
          secs += 1;
          if(lmeters+rmeters >= k) return secs;
      }
  }
}

int main() {
    freopen("race.in", "r", stdin);
    freopen("race.out", "w", stdout);
    int k,n;
    scanf("%d %d", &k, &n);
    for(int i = 0; i < n; i++) {
        printf("%d\n", solve(k));
    }
}
