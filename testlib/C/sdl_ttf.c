#include <SDL/SDL_ttf.h>
#include <stdlib.h>

int	main(int ac, char** av)
{
	TTF_Init();
	TTF_WasInit();
	TTF_Quit();
	TTF_OpenFont(NULL, 0);

	return (0);
}
