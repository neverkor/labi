#include <iostream>
#include <math.h>
using namespace std;

float a, x_max, x, g, f, y, step_value;
int choose, step, count = 0;

void calc()
{
	switch (choose)
	{
		case 1:	g = 10*(-45*a*a+49*a*x+6*x*x)/15*a*a+49*a*x+24*x*x; cout << "g = " << g << endl; break;
		case 2:	f = tan(5*a*a+34*a*x+45*x*x); cout << "f = " << f << endl; break;
		case 3:	y = -asin(7*a*a-a*x-8*x*x); cout << "y = " << y << endl; break;
		default: cout << "Net takoy funkcii." << endl; break;
	}
}

int main()
{
	cout << "Vvedite a: ";
	cin >> a;
	cout << "Vvedite min x: ";
	cin >> x;
	cout << "Vvedite max x: ";
	cin >> x_max;
	while (x > x_max)
	{
		cout << "Min x bolshe max x. Povtorite vvod" << endl;
		cout << "Vvedite min x: ";
		cin >> x;
		cout << "Vvedite max x: ";
		cin >> x_max;
	}
	cout << "Vvedite kol-vo shagov: ";
	cin >> step;
	cout << "Vvedite velichinu shaga: ";
	cin >> step_value;
	cout << "1 - funkciya G\n2 - funkciya F\n3 - funkciya Y\nViberite funkciu: ";
	cin >> choose;
	while (count < step)
	{
		calc();
		if (x > x_max)
		{
			cout << "Oshibka. X previsil max znachenie." << endl;
			break;
		}
		else
		{
			x += step_value;
			count += 1;
		}
	}
	return 0;
}

