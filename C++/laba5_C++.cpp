#include <iostream>
#include <cstdlib>
#include <math.h>
using namespace std;

float a, x_max, x, g, f, y, step_value, search;
char a_ch[255], x_ch[255], x_max_ch[255], step_ch[255], step_value_ch[255], result_ch[255];
int even, num, step, choose, count = 0, coin = 0;
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
	cin >> a_ch;
	a = atof(a_ch);
	cout << "Vvedite min x: ";
	cin >> x_ch;
	x = atof(x_ch);
	cout << "Vvedite max x: ";
	cin >> x_max_ch;
	x_max = atof(x_max_ch);
	
	while (x > x_max)
	{
		cout << "Min x bolshe max x. Povtorite vvod" << endl;
		cout << "Vvedite min x: ";
		cin >> x_ch;
		x = atof(x_ch);
		cout << "Vvedite max x: ";
		cin >> x_max_ch;
		x_max = atof(x_max_ch);
	}
	
	cout << "Vvedite kol-vo shagov: ";
	cin >> step_ch;
	step = atoi(step_ch);
	cout << "Vvedite velichinu shaga: ";
	cin >> step_value_ch;
	step_value = atof(step_value_ch);
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
	
//	cout << endl << "Realnie znacheniya: " << endl;
//	for (int i; i < count; ++i)
//	{
//		cout << result[i] << endl;
//	}
	
	for (int i; i < count; ++i)
	{
		itoa (result[i], result_ch, 10);
		cout << endl << "Realnoe znachenie: " << result[i] << endl;
		cout << "Rezultat v strokovom formate: " << result_ch << endl << endl;
	}
	
    cout << endl << "Vvedite chislo dlya poiska: ";
    cin >> search;
    
	for (int i = 0; i < step; i++)
 	{
 		if (result[i] == search)
 		{
 			coin + 1;
		}
	}
	cout << "Naideno sovpadenii: " << coin << endl;
	 
	cout << endl << "Vvedite chislo, poschitaem chetnie cifri: ";
	cin >> num;
	
	while (num > 0)
	{
		if (num % 2 == 0)
		{
			even += 1;
		}
		num = num / 10;
	}
    cout << "Chetnih cifr " << even << endl;
    
	return 0;
}

