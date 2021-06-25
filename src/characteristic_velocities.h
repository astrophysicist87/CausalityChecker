#ifndef CHARACTERISTIC_VELOCITIES_H
#define CHARACTERISTIC_VELOCITIES_H

#include <cmath>
#include <iostream>

using namespace std;

extern double e, p, cs2;
extern double eta, zeta, tau_pi, tau_Pi;
extern double delta_PiPi, lambda_Pipi, delta_pipi, lambda_piPi, tau_pipi;

double get_g(double Lambda_a)
{
	return ( ( 2.0*(2.0*eta + lambda_piPi*Pi) + tau_pipi*Lambda_a )
			/ ( 4.0*(e+p+Pi)*tau_pi ) );
}

double get_S10(double Lambda_a, double Lambda_d)
{
	return ( ( 2.0*(2.0*eta + lambda_piPi*Pi) + tau_pipi*(Lambda_a+Lambda_d) )
			/ ( 4.0*(e+p+Pi+Lambda_a)*tau_pi ) );
}


double get_S11(double Lambda_d)
{
	double term1      = ( (2.0*eta + lambda_piPi*Pi) + tau_pipi*Lambda_d )
						  / ( 2.0*(e+p+Pi+Lambda_d)*tau_pi );
	double term2num_a = (2.0*eta + lambda_piPi*Pi+(6.0*delta_pipi-tau_pipi)*Lambda_d) / (6.0*tau_pi);
	double term2num_b = (zeta + delta_PiPi*Pi + lambda_Pipi*Lambda_d)/tau_Pi;
	double term2num_c = (e+p+Pi+Lambda_d)*cs2;
	double term2den   = e+p+Pi+Lambda_d

	return ( term1 + (term2num_a + term2num_b + term2num_c) / term2den );
}





#endif
