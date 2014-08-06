#include <gtk/gtk.h>
#include <stdlib.h>

int	main(int ac, char** av)
{
	gtk_init(&ac, &av);
	gtk_window_new(GTK_WINDOW_TOPLEVEL);
	gtk_main();
	gtk_main_quit();
	return (0);
}
