class Kata
{
public:
    std::vector<std::string> towerBuilder(int nFloors)
    {
        std::vector<std::string> result;
        std::string floor;
        int elementsCount = 2 * nFloors - 1;
        for(int i = 0; i < nFloors; ++i)
        {
          for(int j = 0; j < elementsCount; ++j)
          {
            floor += '*';
          }
          while(floor.size() != 2 * nFloors - 1)
          {
            floor.insert(floor.begin(), ' ');
            floor.insert(floor.end(), ' ');
          }
          result.insert(result.begin(), floor);
          floor.clear();
          elementsCount -= 2;
        }
        return result;
    }
};