#include <png.h>
#include <stdlib.h>

int	main(int ac, char** av)
{
	png_init_io(NULL, NULL);
	png_set_sig_bytes(NULL, 0);
	png_get_rows(NULL, NULL);
	png_set_gamma(NULL, 0.0, 0);

	return (0);
}
