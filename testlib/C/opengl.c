#include <GL/gl.h>
#include <stdlib.h>

int	main(int ac, char** av)
{
	glBegin(GL_TRIANGLES);
	glVertex3f(0.0f, 0.0f, 0.0f);
	glEnd();

	return (0);
}
