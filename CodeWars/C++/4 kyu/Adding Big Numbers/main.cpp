
std::string add(std::string a, std::string b) {
  bool isCarry = false;
  int number = 0;
  int size = std::max(a.size(), b.size());
  std::string result;
  int firstDigit = 0;
  int secondDigit = 0;
  
  std::reverse(a.begin(), a.end());
  std::reverse(b.begin(), b.end());
  
  for(int i = 0; i < size; ++i) {
    firstDigit = i < a.size() ? int(a[i]) - '0' : 0;
    secondDigit = i < b.size() ? int(b[i]) - '0' : 0;
    number = firstDigit + secondDigit + isCarry;
    
    if(number >= 10) {
      isCarry = true;
      number %= 10;
    }
    else isCarry = false;
    result += std::to_string(number);
  }
  
  if(isCarry) result += '1';
  std::reverse(result.begin(), result.end());
  auto it = result.begin();
  while(*it == '0' && result.size() > 1) ++it;
  return std::string(it, result.end());
}