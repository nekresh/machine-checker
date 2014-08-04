#include <openssl/ssl.h>
#include <stdlib.h>

int	main(int ac, char** av)
{
	SSL_accept(NULL);
	SSL_add_client_CA(NULL, NULL);
	SSL_clear(NULL);
	SSL_connect(NULL);
	SSL_copy_session_id(NULL, NULL);
	SSL_dup(NULL);
	SSL_get_error(NULL, 0);
	SSL_get_fd(NULL);
	SSL_get_version(NULL);

	return (0);
}
