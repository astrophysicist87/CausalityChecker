#ifndef NECESSARY_CONDITIONS_H
#define NECESSARY_CONDITIONS_H

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <iomanip>
#include <string>

using namespace std;

extern bool test_mode;

extern double tau, x, y;
extern double T, e, p, cs2;
extern double eta, zeta, tau_pi, tau_Pi;
extern double pi00, pi01, pi02, pi11, pi12, pi22, pi33, Pi;
extern double delta_PiPi, lambda_Pipi, delta_pipi, lambda_piPi,
       phi_7, tau_pipi, Tr_pi_sigma;

extern double Lambda_0, Lambda_1, Lambda_2, Lambda_3;

bool check_necessary_condition_0()
{
	if (test_mode)
		cout << "Check " << __FUNCTION__ << ": " << (2.0*eta + lambda_piPi*Pi) - 0.5*tau_pipi*abs(Lambda_1) << endl;
	//cout << "Check " << __FUNCTION__ << ": "
	//	<< (2.0*eta + lambda_piPi*Pi) << " - " << 0.5*tau_pipi*abs(Lambda_1) << " >= 0 " << endl;
	return ( (2.0*eta + lambda_piPi*Pi) - 0.5*tau_pipi*abs(Lambda_1) >= 0.0 );
}

bool check_necessary_condition_1()
{
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< e + p + Pi - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*Lambda_3/(4.0*tau_pi) << endl;

	//cout << "Check " << __FUNCTION__ << ": "
	//	<< e + p + Pi
	//	<< " - " << (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi)
	//	<< " - " << tau_pipi*Lambda_3/(4.0*tau_pi)
	//	<< " >= 0 " << endl;
	return ( e + p + Pi - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*Lambda_3/(4.0*tau_pi) >= 0.0 );
}

bool check_necessary_condition_2()
{
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) + tau_pipi*(Lambda_1 + Lambda_2)/(4.0*tau_pi) << endl;
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) + tau_pipi*(Lambda_1 + Lambda_3)/(4.0*tau_pi) << endl;
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) + tau_pipi*(Lambda_2 + Lambda_3)/(4.0*tau_pi) << endl;

	//cout << "Check " << __FUNCTION__ << "(a): "
	//	<< (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) << " + " << tau_pipi*(Lambda_1 + Lambda_2)/(4.0*tau_pi) << " >= 0 " << endl;
	//cout << "Check " << __FUNCTION__ << "(b): "
	//	<< (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) << " + " << tau_pipi*(Lambda_1 + Lambda_3)/(4.0*tau_pi) << " >= 0 " << endl;
	//cout << "Check " << __FUNCTION__ << "(c): "
	//	<< (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) << " + " << tau_pipi*(Lambda_2 + Lambda_3)/(4.0*tau_pi) << " >= 0 " << endl;
	return ( 
			(2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) + tau_pipi*(Lambda_1 + Lambda_2)/(4.0*tau_pi) >= 0.0
		and (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) + tau_pipi*(Lambda_1 + Lambda_3)/(4.0*tau_pi) >= 0.0
		and (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) + tau_pipi*(Lambda_2 + Lambda_3)/(4.0*tau_pi) >= 0.0
		 );
}

bool check_necessary_condition_3()
{
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< e + p + Pi + Lambda_1 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*(Lambda_1 + Lambda_2)/(4.0*tau_pi) << endl;
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< e + p + Pi + Lambda_1 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*(Lambda_1 + Lambda_3)/(4.0*tau_pi) << endl;
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< e + p + Pi + Lambda_2 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*(Lambda_2 + Lambda_1)/(4.0*tau_pi) << endl;
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< e + p + Pi + Lambda_2 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*(Lambda_2 + Lambda_3)/(4.0*tau_pi) << endl;
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< e + p + Pi + Lambda_3 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*(Lambda_3 + Lambda_1)/(4.0*tau_pi) << endl;
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< e + p + Pi + Lambda_3 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*(Lambda_3 + Lambda_2)/(4.0*tau_pi) << endl;
	return ( 
			e + p + Pi + Lambda_1 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*(Lambda_1 + Lambda_2)/(4.0*tau_pi) >= 0.0
		and e + p + Pi + Lambda_1 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*(Lambda_1 + Lambda_3)/(4.0*tau_pi) >= 0.0
		and e + p + Pi + Lambda_2 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*(Lambda_2 + Lambda_1)/(4.0*tau_pi) >= 0.0
		and e + p + Pi + Lambda_2 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*(Lambda_2 + Lambda_3)/(4.0*tau_pi) >= 0.0
		and e + p + Pi + Lambda_3 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*(Lambda_3 + Lambda_1)/(4.0*tau_pi) >= 0.0
		and e + p + Pi + Lambda_3 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*(Lambda_3 + Lambda_2)/(4.0*tau_pi) >= 0.0
		 );
}

bool check_necessary_condition_4()
{
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) + tau_pipi*Lambda_1/(2.0*tau_pi)
				+ (2.0*eta + lambda_piPi*Pi + (6.0*delta_pipi - tau_pipi)*Lambda_1)/(6.0*tau_pi)
				+ (zeta + delta_PiPi*Pi + lambda_Pipi*Lambda_1)/tau_Pi
				+ (e + p + Pi + Lambda_1)*cs2 << endl;
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) + tau_pipi*Lambda_2/(2.0*tau_pi)
				+ (2.0*eta + lambda_piPi*Pi + (6.0*delta_pipi - tau_pipi)*Lambda_2)/(6.0*tau_pi)
				+ (zeta + delta_PiPi*Pi + lambda_Pipi*Lambda_2)/tau_Pi
				+ (e + p + Pi + Lambda_2)*cs2 << endl;
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) + tau_pipi*Lambda_3/(2.0*tau_pi)
				+ (2.0*eta + lambda_piPi*Pi + (6.0*delta_pipi - tau_pipi)*Lambda_3)/(6.0*tau_pi)
				+ (zeta + delta_PiPi*Pi + lambda_Pipi*Lambda_3)/tau_Pi
				+ (e + p + Pi + Lambda_3)*cs2 << endl;

	return ( 
			(2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) + tau_pipi*Lambda_1/(2.0*tau_pi)
				+ (2.0*eta + lambda_piPi*Pi + (6.0*delta_pipi - tau_pipi)*Lambda_1)/(6.0*tau_pi)
				+ (zeta + delta_PiPi*Pi + lambda_Pipi*Lambda_1)/tau_Pi
				+ (e + p + Pi + Lambda_1)*cs2 >= 0.0
		and (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) + tau_pipi*Lambda_2/(2.0*tau_pi)
				+ (2.0*eta + lambda_piPi*Pi + (6.0*delta_pipi - tau_pipi)*Lambda_2)/(6.0*tau_pi)
				+ (zeta + delta_PiPi*Pi + lambda_Pipi*Lambda_2)/tau_Pi
				+ (e + p + Pi + Lambda_2)*cs2 >= 0.0
		and (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) + tau_pipi*Lambda_3/(2.0*tau_pi)
				+ (2.0*eta + lambda_piPi*Pi + (6.0*delta_pipi - tau_pipi)*Lambda_3)/(6.0*tau_pi)
				+ (zeta + delta_PiPi*Pi + lambda_Pipi*Lambda_3)/tau_Pi
				+ (e + p + Pi + Lambda_3)*cs2 >= 0.0
		 );
}

bool check_necessary_condition_5()
{
	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< e + p + Pi + Lambda_1 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*Lambda_1/(2.0*tau_pi)
				- (2.0*eta + lambda_piPi*Pi + (6.0*delta_pipi - tau_pipi)*Lambda_1)/(6.0*tau_pi)
				- (zeta + delta_PiPi*Pi + lambda_Pipi*Lambda_1)/tau_Pi
				- (e + p + Pi + Lambda_1)*cs2 << endl;

	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< e + p + Pi + Lambda_2 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*Lambda_2/(2.0*tau_pi)
				- (2.0*eta + lambda_piPi*Pi + (6.0*delta_pipi - tau_pipi)*Lambda_2)/(6.0*tau_pi)
				- (zeta + delta_PiPi*Pi + lambda_Pipi*Lambda_2)/tau_Pi
				- (e + p + Pi + Lambda_2)*cs2 << endl;

	if (test_mode)
	cout << "Check " << __FUNCTION__ << ": "
		<< e + p + Pi + Lambda_3 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*Lambda_3/(2.0*tau_pi)
				- (2.0*eta + lambda_piPi*Pi + (6.0*delta_pipi - tau_pipi)*Lambda_3)/(6.0*tau_pi)
				- (zeta + delta_PiPi*Pi + lambda_Pipi*Lambda_3)/tau_Pi
				- (e + p + Pi + Lambda_3)*cs2 << endl;

	return ( 
			e + p + Pi + Lambda_1 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*Lambda_1/(2.0*tau_pi)
				- (2.0*eta + lambda_piPi*Pi + (6.0*delta_pipi - tau_pipi)*Lambda_1)/(6.0*tau_pi)
				- (zeta + delta_PiPi*Pi + lambda_Pipi*Lambda_1)/tau_Pi
				- (e + p + Pi + Lambda_1)*cs2 >= 0.0
		and e + p + Pi + Lambda_2 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*Lambda_2/(2.0*tau_pi)
				- (2.0*eta + lambda_piPi*Pi + (6.0*delta_pipi - tau_pipi)*Lambda_2)/(6.0*tau_pi)
				- (zeta + delta_PiPi*Pi + lambda_Pipi*Lambda_2)/tau_Pi
				- (e + p + Pi + Lambda_2)*cs2 >= 0.0
		and e + p + Pi + Lambda_3 - (2.0*eta + lambda_piPi*Pi)/(2.0*tau_pi) - tau_pipi*Lambda_3/(2.0*tau_pi)
				- (2.0*eta + lambda_piPi*Pi + (6.0*delta_pipi - tau_pipi)*Lambda_3)/(6.0*tau_pi)
				- (zeta + delta_PiPi*Pi + lambda_Pipi*Lambda_3)/tau_Pi
				- (e + p + Pi + Lambda_3)*cs2 >= 0.0
		 );
}

void check_necessary_conditions(vector<bool> & necessary_conditions)
{
	necessary_conditions[0] = check_necessary_condition_0();
	necessary_conditions[1] = check_necessary_condition_1();
	necessary_conditions[2] = check_necessary_condition_2();
	necessary_conditions[3] = check_necessary_condition_3();
	necessary_conditions[4] = check_necessary_condition_4();
	necessary_conditions[5] = check_necessary_condition_5();

	return;
}

#endif
