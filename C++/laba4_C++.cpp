#include <iostream>
#include <math.h>
using namespace std;

float a, x_max, x, g, f, y, step_value, max_value, min_value;
int choose, step, count = 0;
float *result = new float[step];

void calc()
{
	switch (choose)
	{
		case 1:
			g = 10*(-45*a*a+49*a*x+6*x*x)/15*a*a+49*a*x+24*x*x;
			result[count] = g;
			break;
		case 2:
			f = tan(5*a*a+34*a*x+45*x*x);
			result[count] = f;
			break;
		case 3:
			y = -asin(7*a*a-a*x-8*x*x);
			result[count] = y;
			break;
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
	cout << "1 - funkciya G" << endl << "2 - funkciya F" << endl << "3 - funkciya Y" << endl << "Viberite funkciu: ";
	cin >> choose;
	
	while (count < step)
	{
		calc();
		if (x > x_max)
		{
			cout << "Oshibka. X previsil max znachenie.";
			break;
		}
		else
		{
			x += step_value;
			count += 1;
		}
	}
	
	cout << endl << "Rezultati:" << endl;
	for (int i; i < count; ++i)
	{
		cout << result[i] << endl;
	}
	
	min_value = result[0];
	max_value = result[0];
	
	for (int i = 0; i < count; ++i)
	{
        if (result[i] > max_value)
		{
            max_value = result[i];
        }
    }
    
    for (int i = 0; i < count; ++i)
	{
        if (result[i] < min_value)
		{
            min_value = result[i];
        }
    }
    
    cout << endl << "Min znachenie: " << min_value << endl;
    cout << "Max znachenie: " << max_value << endl;
    
	return 0;
}

