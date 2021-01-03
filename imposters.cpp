#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int main() {
    ifstream fin("imposters.in");
    ofstream fout("imposters.out");
    int n;
    fin >> n;
    int numfreq[10001];
    int array[n];
    for(int i=0; i<n; i++) {
        fin >> array[i];
        numfreq[array[i]]++;
    }
    int max = 0;
    int maxn = -1;
    int before = array[0];
    int counter = 0;
    int currnum;
    for(int i=0; i<n; i++) {
        while(i<n && array[i] == before) {
            currnum = array[i];
            before = array[i];
            counter++;
            i++;
        }
        if(counter > max) {
            max = counter;
            maxn = currnum;
        }
        before = array[i];
        counter = 0;
    }
    fout << numfreq[maxn];
}
