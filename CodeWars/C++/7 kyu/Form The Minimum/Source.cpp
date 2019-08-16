#include <vector>
#include <set>
#include <algorithm>

using namespace std; 

unsigned long long minValue (vector <int> values)
{
  set<int> uniq_values;
  copy(values.begin(), values.end(), inserter(uniq_values, uniq_values.end()));
  string result;
  while(!uniq_values.empty())
  {
    result += to_string(*uniq_values.begin());
    uniq_values.erase(uniq_values.begin());
  }
  return stoi(result); 
}