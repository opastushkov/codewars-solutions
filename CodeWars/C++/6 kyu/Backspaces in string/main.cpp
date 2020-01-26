std::string cleanString(const std::string &s) {
    auto backspace_count = 0;
    std::string result;
    for(auto it = s.rbegin(); it < s.rend(); it++)
    {
      if(*it == '#') ++backspace_count;
      else if(backspace_count > 0) --backspace_count;
      else result += *it;
    }
    std::reverse(result.begin(), result.end());
    return result;
}