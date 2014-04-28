#include <stdlib.h>
#include <wand/MagickWand.h>

int main(int ac, char** av)
{
    MagickWandGenesis();
    NewMagickWand();
    MagickReadImage(NULL, NULL);
    return (0);
}
