#include <iostream>
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;

float centr_x, centr_y, radius, key_x, key_y, point_x;
int point, enter, not_enter, enter_x;
float *x = new float[point];
float *y = new float[point];
float *result_x = new float[point];
float *result_y = new float[point];
float *result = new float[point];

void calc()
{
	for (int i = 0; i < point; i++)
	{
		key_x = (x[i] - centr_x) * (x[i] - centr_x);
		result_x[i] = key_x;
	}
	for (int i = 0; i < point; i++)
	{
		key_y = (y[i] - centr_y) * (y[i] - centr_y);
		result_y[i] = key_y;
	}
	for (int i = 0; i < point; i++)
	{
		result[i] = result_x[i] + result_y[i];
	}
	for (int i =0; i < point; i++)
	{
		if (result[i] <= radius * radius)
		{
			enter += 1;
		}
		else
		{
			not_enter += 1;
		}
	}
	cout << endl << "Vhodit ili lezhit na okruzhnosti tochek: " << enter << endl;
	cout << endl << "Ne vhodit v okruzhnost: " << not_enter << endl;
	cout << endl << "Centr okruzhnosti: x: " << centr_x << " ; y: " << centr_y << endl;
	cout << endl << "Tochek vsego: " << point << endl;
}

void search()
{
	cout << endl << "Vvedite koordinaty X dlya poiska tochek: ";
	cin >> point_x;
	for (int i = 0; i < point; i++)
	{
		if (x[i] == point_x)
		{
			enter_x += 1;
		}
	}
	cout << endl << "Na etoi koordinate naideno tochek: " << enter_x << endl;
}

int main()
{
	cout << "Vvedite koordinatu X dlya centra okruzhnosti: ";
	cin >> centr_x;
	cout << "Vvedite koordinatu Y dlya centra okruzhnosti: ";
	cin >> centr_y;
	cout << "Vvedite radius okruzhnosti: ";
	cin >> radius;
	cout << "Vvedite kol-vo tochek: ";
	cin >> point;
	
	for (int i = 0; i < point; ++i)
	{
		x[i] = rand() % 101 - 50; // диапазон от -50 до 50
	}
	for (int i = 0; i < point; ++i)
	{
		y[i] = rand() % 101 - 50;
	}
	
	calc();
	search();
	
	float time = clock() / 1000.0;
	
	ofstream fout("time.txt");
	fout << "Vremya vipolneniya: " << time << " s" << endl;
	fout.close();
	cout << endl << "Vremya vipolneniya zapisano v time.txt" << endl;
	
	return 0;
}
