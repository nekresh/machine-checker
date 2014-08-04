#include <SDL_mixer.h>
#include <stdlib.h>

int	main(int ac, char** av)
{
	Mix_Init(0);
	Mix_OpenAudio(0, 0, 0, 0);
	Mix_Quit();

	return (0);
}
