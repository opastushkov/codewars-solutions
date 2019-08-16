std::string bumps(std::string road){
  return count(road.begin(), road.end(), 'n') > 15 ? "Car Dead" : "Woohoo!";
}