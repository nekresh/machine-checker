#include <QApplication>
#include <QTextEdit>

int	main(int ac, char** av)
{
	QApplication	app(ac, av);

	QTextEdit	textEdit;
	textEdit.show();

	return app.exec();
}
