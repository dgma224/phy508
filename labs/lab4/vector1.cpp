#include <iostream>
#include <vector>
using namespace std;

int main (void)
{


  vector <int> v1;
  vector <int> v2(2,4);

  v1.resize(10,2);

  cout <<"v1 "<<endl;
  for(int i=0;i<v1.size();i++)
    cout <<v1.at(i)<<" "<<v1[i]<<endl;




  cout <<"v2 initially "<<endl;
  for(int i=0;i<v2.size();i++)
    cout <<i<<" "<<v2[i]<<endl;

  for (int i=0;i<7;i++)
    v2.push_back(i*i);


  cout <<"v2 updated after push back "<<endl;
  for(int i=0;i<v2.size();i++)
    cout <<i<<" "<<v2[i]<<endl;

}

