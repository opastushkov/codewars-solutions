std::string bingo(std::vector<std::pair<std::string, int>> ticket, int win)
{
  auto mini_wins_counter = 0;
  for(auto it: ticket)
  {
    if(it.first.find(char(it.second)) != std::string::npos) ++mini_wins_counter;
  }
  return mini_wins_counter >= win ? "Winner!" : "Loser!";
}