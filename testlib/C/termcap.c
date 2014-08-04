#include <ncurses/curses.h>
#include <term.h>
#include <stdlib.h>

int	main(int ac, char** av)
{
	tgetent(NULL, NULL);
	tgetstr(NULL, NULL);
	tgoto(NULL, 0, 0);
	tputs(NULL, 0, NULL);

	return (0);
}
