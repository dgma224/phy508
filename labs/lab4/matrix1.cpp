#include <iostream>
#include <vector>
using namespace std;

int main (void)
{

  vector<vector<int> > mat1;

  // MAKE A 4x4 MATRIX WITH 6's IN EACH ENTRY
  mat1.resize(4,vector <int> (4,6));
  // CHANGE 3rd ROW to HAVE 3 COLUMNS OF 2's
  mat1[0]=vector <int>(1,1);
  mat1[1]=vector <int>(3,2);
  mat1[2]=vector <int>(1,3);
  mat1[3]=vector <int>(4,4);
  
  
  // PRINT ASSIGNED VALUES
  for (int i=0;i<mat1.size();i++)
    {
      for (int j=0;j<mat1.at(i).size();j++)
	cout <<mat1[i][j]<<" ";
      cout << endl;
    }
}


