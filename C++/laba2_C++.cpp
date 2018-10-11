#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	float a, x, g, f, y;
	int choose;
	cout << "Vvedite a: ";
	cin >> a;
	cout << "Vvedite x: ";
	cin >> x;
	cout << "1 - funkciya G\n2 - funkciya F\n3 - funkciya Y\nViberite funkciu: ";
	cin >> choose;
	switch (choose)
	{
		case 1: g = 10*(-45*a*a+49*a*x+6*x*x)/15*a*a+49*a*x+24*x*x; cout << "g = " << g << endl; break;
		case 2: f = tan(5*a*a+34*a*x+45*x*x); cout << "f = " << f << endl; break;
		case 3: y = -asin(7*a*a-a*x-8*x*x); cout << "y = " << y << endl; break;
		default: cout << "Net takoy funkcii." << endl; break;
	}
	return 0;
}

