#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	float a, x, g, f, y;
	cout << "Vvedite a: ";
	cin >> a;
	cout << "Vvedite x: ";
	cin >> x;
	g = 10*(-45*a*a+49*a*x+6*x*x)/15*a*a+49*a*x+24*x*x;
	f = tan(5*a*a+34*a*x+45*x*x);
	y = -asin(7*a*a-a*x-8*x*x);
	cout << "g = " << g << endl;
	cout << "f = " << f << endl;
	cout << "y = " << y << endl;
	return 0;
}

