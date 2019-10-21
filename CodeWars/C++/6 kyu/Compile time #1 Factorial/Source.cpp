template <int x>
struct factorial {
  static const unsigned long long value = factorial<x - 1>::value * x;
};

template <>
struct factorial<0> {
  static const unsigned long long value = 1;
};

template <int x> const unsigned long long factorial<x>::value;
const unsigned long long factorial<0>::value;
