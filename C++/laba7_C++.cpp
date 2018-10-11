#include <iostream>
#include <cstdlib>
#include <math.h>
#include <cstring>
#include <fstream>
using namespace std;

struct Result
{
	char name_func_g[5];
	char name_func_f[5];
	char name_func_y[5];
	float value_func_g;
	float value_func_f;
	float value_func_y;
};

float a, x_max, x, g, f, y, step_value;
char a_ch[50], x_ch[50], x_max_ch[50], step_ch[50], step_value_ch[50], result_ch[50], file_result[50];
int even, num, step, count = 0;
Result *result = new Result[step];

void calc()
{
	g = 10*(-45*a*a+49*a*x+6*x*x)/15*a*a+49*a*x+24*x*x;
	strcpy(result[count].name_func_g, "G");
	result[count].value_func_g = g;
	f = tan(5*a*a+34*a*x+45*x*x);
	strcpy(result[count].name_func_f, "F");
	result[count].value_func_f = f;
	y = -asin(7*a*a-a*x-8*x*x);
	strcpy(result[count].name_func_y, "Y");
	result[count].value_func_y = y;
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
	
	ofstream fout("result.txt");
	for (int i = 0; i < step; i++)
	{
		fout << result[i].name_func_g << " = " << result[i].value_func_g << endl;
		fout << result[i].name_func_f << " = " << result[i].value_func_f << endl;
		fout << result[i].name_func_y << " = " << result[i].value_func_y << endl;
	}
	fout.close();

	for (int i = 0; i < step; i++)
	{
		strcpy(result[i].name_func_g, "0");
		strcpy(result[i].name_func_f, "0");
		strcpy(result[i].name_func_y, "0");
		result[i].value_func_g = 0;
		result[i].value_func_f = 0;
		result[i].value_func_y = 0;
	}
	
	ifstream fin("result.txt");
	while (!fin.eof())
	{
		fin.getline(file_result, 255);
		cout << file_result << endl;
	}
	fin.close();
	
	return 0;
}

