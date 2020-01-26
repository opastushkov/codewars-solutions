std::string my_first_interpreter(const std::string& code)
{
  char memory_cell = 0;
  std::string result;
  for(auto it = code.begin(); it < code.end(); ++it)
    if(*it == '+') ++memory_cell;
    else if(*it == '.') result += memory_cell;
  return result;
}
