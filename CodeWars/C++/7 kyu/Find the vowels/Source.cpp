#include <set>

std::set<char> cVowels = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'};

std::vector<int> vowelIndices(std::string word)
{
  std::vector<int> res; 
  for(auto i = 0; i < word.size(); ++i)
    if(cVowels.count(word[i]))
      res.push_back(i + 1);
	return res;
}