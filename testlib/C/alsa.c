#include <stdlib.h>
#include <asound.h>

int main(int ac, char** av)
{
    snd_pcm_hw_params_any(NULL, NULL);
    snd_pcm_hw_params_set_rate_resample(NULL, NULL, 0);
    return (0);
}
