#pragma once
#include <iostream>
#include <conio.h>

using namespace std;
using namespace System;

class CMovimiento{
protected:
	int x, y;
	int dx, dy;
	int ancho, alto;

public:
	CMovimiento(){ //CONSTRUCTOR PARA POSICIONES DE TRANSPORTES
		x = rand() % 60 + 14;
		y = rand() % 50 + 6;
	}

	CMovimiento(int x, int y){ //CONSTRUCTOR PARA POSICIONES DE LA PERSONA
		this->x = x;
		this->y = y;
	}

	~CMovimiento(){}

	void moverTransporte() {
		if (x <= 3 || x + ancho >= 100)dx *= -1;
		x += dx;
	}
};