#include <string>
#include <vector>
#include <algorithm>

int deleteDigit(int n)
{
  std::string s = std::to_string(n);
  std::vector<int> combinations;
  for(int i = 0; i < s.size(); ++i)
  {
    std::string tmp;
    for(int j = 0; j < s.size(); ++j)
    {
        if(j != i) tmp += s[j];
    }
    combinations.push_back(std::stoi(tmp));
  }
  return *std::max_element(combinations.begin(), combinations.end());
}