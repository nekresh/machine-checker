#include <regex>

int	main(int ac, char** av)
{
	std::regex r("(\\S+)");
	std::regex_search(std::string("Hello world"), r);

	return (0);
}
