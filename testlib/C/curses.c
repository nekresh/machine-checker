#include <curses.h>
#include <stdlib.h>

int	main(int ac, char** av)
{
	initscr();
	nonl();
	cbreak();
	echo();
	has_colors();
	start_color();
	getch();
	endwin();

	return (0);
}
