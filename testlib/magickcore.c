#include <stdlib.h>
#include <magick/MagickCore.h>

int main(int ac, char** av)
{
    MagickCoreGenesis(NULL, MagickTrue);
    AcquireExceptionInfo();
    CloneImageInfo(NULL);
    return (0);
}
