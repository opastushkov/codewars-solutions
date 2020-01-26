std::pair<std::size_t, std::size_t> two_sum(const std::vector<int>& numbers, int target) {
    for (auto i = 0; i < numbers.size(); ++i)
      for (auto j = 0; j < numbers.size(); ++j)
        if (i != j && numbers[i] + numbers[j] == target)
          return std::pair<std::size_t, std::size_t> (i, j);
}