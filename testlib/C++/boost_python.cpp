#include <boost/python.hpp>

char const*	greet()
{
	return "hello world";
}

BOOST_PYTHON_MODULE(hello_ext)
{
	using namespace boot::python;
	def("greet", greet);
}

int	main(int ac, char** av)
{
	return (0);
}
