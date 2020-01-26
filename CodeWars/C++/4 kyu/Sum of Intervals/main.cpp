#include <vector>
#include <utility>
#include <numeric>

int sum_intervals(std::vector<std::pair<int, int>> intervals) {
  std::vector<int> numbers;
  for(auto it: intervals) {
    for(auto i = it.first; i < it.second; ++i) {
      if(std::find(numbers.begin(), numbers.end(), i) == numbers.end()) {
        numbers.push_back(i);
        }
    }
  }
  
  return numbers.size();
}