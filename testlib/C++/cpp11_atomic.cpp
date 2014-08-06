#include <atomic>

int	main(int ac, char** av)
{
	std::atomic_int	i;

	i.store(10);
	i.load();

	return (0);
}
