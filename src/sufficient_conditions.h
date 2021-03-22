#ifndef SUFFICIENT_CONDITIONS_H
#define SUFFICIENT_CONDITIONS_H

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <iomanip>
#include <string>

extern bool test_mode;

using namespace std;

extern double tau, x, y;
extern double T, e, p, cs2;
extern double eta, zeta, tau_pi, tau_Pi;
extern double pi00, pi01, pi02, pi11, pi12, pi22, pi33, Pi;
extern double delta_PiPi, lambda_Pipi, delta_pipi, lambda_piPi,
       phi_7, tau_pipi, Tr_pi_sigma;

extern double Lambda_0, Lambda_1, Lambda_2, Lambda_3;

bool check_sufficient_condition_0()
{
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< (e + p + Pi - abs(Lambda_1)) - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*Lambda_3/(2.0*tau_pi)
		<< "   "
		<< 0.0 << endl;

	return ( 
			(e + p + Pi - abs(Lambda_1)) - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*Lambda_3/(2.0*tau_pi) >= 0.0
		 );
}

bool check_sufficient_condition_1()
{
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< (2.0*eta + lambda_piPi*Pi) - tau_pipi*abs(Lambda_1)
		<< "   "
		<< 0.0 << endl;

	return ( (2.0*eta + lambda_piPi*Pi) - tau_pipi*abs(Lambda_1) > 0.0 );
}

bool check_sufficient_condition_2()
{
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< tau_pipi
		<< "   "
		<< 6.0*delta_pipi << endl;

	return ( tau_pipi <= 6.0*delta_pipi );
}

bool check_sufficient_condition_3()
{
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< (lambda_Pipi/tau_Pi) + cs2 - tau_pipi/(12.0*tau_pi)
		<< "   "
		<< 0.0 << endl;

	return ( (lambda_Pipi/tau_Pi) + cs2 - tau_pipi/(12.0*tau_pi) >= 0.0 );
}

bool check_sufficient_condition_4()
{
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< (4.0*eta + 2.0*lambda_piPi*Pi + (3.0*delta_pipi + tau_pipi)*Lambda_3)/(3.0*tau_pi)
				+ (zeta + delta_PiPi*Pi + lambda_Pipi*Lambda_3)/tau_Pi + abs(Lambda_1) + Lambda_3*cs2
				+ ( ( (12.0*delta_pipi - tau_pipi)/(12.0*tau_pi) )
					* ( (lambda_Pipi/tau_Pi) + cs2 - tau_pipi/(12.0*tau_pi) )
					* ( abs(Lambda_1) + Lambda_3 )*( abs(Lambda_1) + Lambda_3 ) )
				  / ( e + p + Pi - abs(Lambda_1) - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*Lambda_3/(2.0*tau_pi) )
		<< "   "
		<< (e + p + Pi) * (1.0-cs2) << endl;

	return ( (4.0*eta + 2.0*lambda_piPi*Pi + (3.0*delta_pipi + tau_pipi)*Lambda_3)/(3.0*tau_pi)
				+ (zeta + delta_PiPi*Pi + lambda_Pipi*Lambda_3)/tau_Pi + abs(Lambda_1) + Lambda_3*cs2
				+ ( ( (12.0*delta_pipi - tau_pipi)/(12.0*tau_pi) )
					* ( (lambda_Pipi/tau_Pi) + cs2 - tau_pipi/(12.0*tau_pi) )
					* ( abs(Lambda_1) + Lambda_3 )*( abs(Lambda_1) + Lambda_3 ) )
				  / ( e + p + Pi - abs(Lambda_1) - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*Lambda_3/(2.0*tau_pi) )
			<= (e + p + Pi) * (1.0-cs2)
 		);
}

bool check_sufficient_condition_5()
{
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< (2.0*eta + lambda_piPi*Pi + (tau_pipi - 6.0*delta_pipi)*abs(Lambda_1))/(6.0*tau_pi)
			+ (zeta + delta_PiPi*Pi - lambda_Pipi*abs(Lambda_1))/tau_Pi
			+ (e + p + Pi - abs(Lambda_1))*cs2
		<< "   "
		<< 0.0 << endl;

	return ( (2.0*eta + lambda_piPi*Pi + (tau_pipi - 6.0*delta_pipi)*abs(Lambda_1))/(6.0*tau_pi)
			+ (zeta + delta_PiPi*Pi - lambda_Pipi*abs(Lambda_1))/tau_Pi
			+ (e + p + Pi - abs(Lambda_1))*cs2 >= 0.0
		);
}

bool check_sufficient_condition_6()
{
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< 1.0
		<< "   "
		<< ( ( (12.0*delta_pipi - tau_pipi)/(12.0*tau_pi) )
					* ( (lambda_Pipi/tau_Pi) + cs2 - tau_pipi/(12.0*tau_pi) )
					* ( abs(Lambda_1) + Lambda_3 )*( abs(Lambda_1) + Lambda_3 ) )
			/ ( ( (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*abs(Lambda_1)/(2.0*tau_pi) )
			   * ( (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*abs(Lambda_1)/(2.0*tau_pi) ) ) << endl;

	return ( ( ( (12.0*delta_pipi - tau_pipi)/(12.0*tau_pi) )
					* ( (lambda_Pipi/tau_Pi) + cs2 - tau_pipi/(12.0*tau_pi) )
					* ( abs(Lambda_1) + Lambda_3 )*( abs(Lambda_1) + Lambda_3 ) )
			<= ( (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*abs(Lambda_1)/(2.0*tau_pi) )
			   * ( (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*abs(Lambda_1)/(2.0*tau_pi) )
		);
}

bool check_sufficient_condition_7()
{
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< (4.0*eta + 2.0*lambda_piPi*Pi - (3.0*delta_pipi + tau_pipi)*abs(Lambda_1))/(3.0*tau_pi)
				+ (zeta + delta_PiPi*Pi - lambda_Pipi*abs(Lambda_1))/tau_Pi + (e + p + Pi - abs(Lambda_1))*cs2
		<< "   "
		<< (e + p + Pi + Lambda_2)*(e + p + Pi + Lambda_3)
				* ( 1.0 + 2.0*( (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) + tau_pipi*Lambda_3/(2.0*tau_pi) )
							/(e + p + Pi - abs(Lambda_1)) )
				/ ( 3.0*(e + p + Pi - abs(Lambda_1)) ) << endl;

	return ( (4.0*eta + 2.0*lambda_piPi*Pi - (3.0*delta_pipi + tau_pipi)*abs(Lambda_1))/(3.0*tau_pi)
				+ (zeta + delta_PiPi*Pi - lambda_Pipi*abs(Lambda_1))/tau_Pi + (e + p + Pi - abs(Lambda_1))*cs2
			>= (e + p + Pi + Lambda_2)*(e + p + Pi + Lambda_3)
				* ( 1.0 + 2.0*( (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) + tau_pipi*Lambda_3/(2.0*tau_pi) )
							/(e + p + Pi - abs(Lambda_1)) )
				/ ( 3.0*(e + p + Pi - abs(Lambda_1)) )
		);
}

void check_sufficient_conditions(vector<bool> & sufficient_conditions)
{
	sufficient_conditions[0] = check_sufficient_condition_0();
	sufficient_conditions[1] = check_sufficient_condition_1();
	sufficient_conditions[2] = check_sufficient_condition_2();
	sufficient_conditions[3] = check_sufficient_condition_3();
	sufficient_conditions[4] = check_sufficient_condition_4();
	sufficient_conditions[5] = check_sufficient_condition_5();
	sufficient_conditions[6] = check_sufficient_condition_6();
	sufficient_conditions[7] = check_sufficient_condition_7();

	return;
}

#endif
