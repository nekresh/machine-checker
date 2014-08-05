#include <boost/spirit/include/qi.hpp>

using namespace boost::spirit;

int	main(int ac, char** av)
{
	double_ >> +double_ >> *lit("hello") >> +!(int_ >> lit("world"));
	return (0);
}
