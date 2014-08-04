#include <jpeglib.h>
#include <stdlib.h>

int	main(int ac, char** av)
{
	jpeg_abort(NULL);
	jpeg_write_tables(NULL);
	jpeg_start_decompress(NULL);
	jpeg_finish_decompress(NULL);

	return (0);
}
