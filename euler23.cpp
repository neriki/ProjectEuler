#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int testAbundant(long n){
    long sum=0;
    for(long i=1;i<((n/2)+1);i++){
        //cout<<i<<" <-- i "<< int(n%i) <<" <-- n%i\n";
        if((n%i)==0)
            sum+=i;
    }
    //cout<<"testAbundant"<<sum<<' '<<n<<'\n';
    if(sum>n)return 1;
    return 0;
}

int test(long num){
    long a,b;
    for(long i=12;i<((num/2)+1);i++){
        a=num-i;
        b=i;
        //cout<<a << ' '<<b<<'\n';
        if(testAbundant(a) && testAbundant(b)){
            return 1;
        }
    }
    return 0;
}

int main() {
    long sum=0;
    for(int i=0;i<28123;i++){
        if(!test(i)){
            sum+=i;
            cout<<"\033[1;31m"<<i<<"\033[0m\t";
        }
        else
        {
            cout<<i<<'\t';
        }
    }
    cout<<"\n\n"<<sum<<'\n';
    return 0;
}

