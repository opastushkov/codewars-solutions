#include <string>

bool board[8][8] = {
  {false, true, false, true, false, true, false, true},
  {true, false, true, false, true, false, true, false},
  {false, true, false, true, false, true, false, true},
  {true, false, true, false, true, false, true, false},
  {false, true, false, true, false, true, false, true},
  {true, false, true, false, true, false, true, false},
  {false, true, false, true, false, true, false, true},
  {true, false, true, false, true, false, true, false}
};

bool chessBoardCellColor(std::string cell1, std::string cell2) {
  std::string num1;
  num1 += cell1[1];
  std::string num2;
  num2 += cell2[1];
  return board[static_cast<int>(cell1[0]) - static_cast<int>('A')][std::stoi(num1) - 1] ==
         board[static_cast<int>(cell2[0]) - static_cast<int>('A')][std::stoi(num2) - 1];
}