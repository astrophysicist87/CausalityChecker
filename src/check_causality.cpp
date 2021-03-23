/////////////////////////////////////////////////////////////////
// Author  - Christopher Plumberg                              //
// Date    - November 24, 2020                                 //
// Purpose - To test whether a given hydro evolution satisfies //
//           general criteria of relativistic causality        //
/////////////////////////////////////////////////////////////////

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <iomanip>
#include <string>

#include <gsl/gsl_math.h>
#include <gsl/gsl_complex.h>
#include <gsl/gsl_eigen.h>

#include "necessary_conditions.h"
#include "sufficient_conditions.h"

using namespace std;

const double epsilon = 1e-4;

bool test_mode;

double tau, x, y;
double T, e, p, cs2;
double eta, zeta, tau_pi, tau_Pi;
double pi00, pi01, pi02, pi11, pi12, pi22, pi33, Pi;
double delta_PiPi, lambda_Pipi, delta_pipi, lambda_piPi,
       phi_7, tau_pipi, Tr_pi_sigma;

double Lambda_0, Lambda_1, Lambda_2, Lambda_3;

bool get_sorted_eigenvalues_of_pi_mu_nu(
		double & Lambda_0, double & Lambda_1, double & Lambda_2, double & Lambda_3 );

int main(int argc, char *argv[])
{
	// turn off errors for now...
	gsl_set_error_handler_off();

	// check input first
	if (argc < 2)
	{
		cout << "<<<=========================================================>>>" << endl;
		cout << "Usage: ./check_causality path_to_input_file" << endl << endl;
		cout << "---------------------------------------------------------------"
			 << endl << "Output per row:" << endl;
		cout << "[necessary conditions passed (binary)] " << endl
                "[sufficient conditions passed (binary)] " << endl
                "tau x y T e [all units in fm] " << endl
                "[all pre-conditions satisfied (binary)] " << endl
                "[diagonalization succeeded (binary)] " << endl << endl;
		cout << "<<<=========================================================>>>" << endl;

		//exit(1);
		test_mode = true;
		
		cout << "----- Printing out diagnostic information below this line -----" << endl;
		cout << setprecision(12);

		// Run test - just pick some values
		tau = 0.0; x = 0.0; y = 0.0;
		pi00 = 3.5078e-7; pi01 = 0.0013504; pi02 = -0.0045209; pi11 = 0.21482;
		pi12 = 0.00048869; pi22 = 0.2144; pi33 = -0.42917;
		//Lambda_0 = 0.0; Lambda_1 = -0.42917; Lambda_2 = 0.214173; Lambda_3 = 0.215151;
		double rands[13] = {0.7486510936, 0.7832718015, 0.6676001377, 0.6540939720, 
							0.1373497793, 0.1484691683, 0.9348005828, 0.7079133674,
							0.9495418450, 0.3749321713, 0.4646400815, 0.8826349161,
							0.6741853064};
		/*e = 0.835978; p = 0.891412; Pi = 0.649474; tau_pi = 0.977974; tau_Pi = 0.756016;
		eta = 0.203962; zeta = 0.776212; tau_pipi = 0.0405803;
		delta_PiPi = 0.763535; lambda_Pipi = 0.650383;
		delta_pipi = 0.656796; lambda_piPi = 0.168251;
		cs2 = 0.305789;*/
		e = rands[0]; p = rands[1]; Pi = rands[2]; tau_pi = rands[3]; tau_Pi = rands[4];
		eta = rands[5]; zeta = rands[6]; tau_pipi = rands[7];
		delta_PiPi = rands[8]; lambda_Pipi = rands[9];
		delta_pipi = rands[10]; lambda_piPi = rands[11];
		cs2 = rands[12];

		Lambda_0 = 0.0; Lambda_1 = 0.0; Lambda_2 = 0.0; Lambda_3 = 0.0;
		bool eigenSuccess = get_sorted_eigenvalues_of_pi_mu_nu(
							Lambda_0, Lambda_1, Lambda_2, Lambda_3 );

		const double enthalpy_plus_Pi = e+p+Pi;

		bool assumptionsSatisfied
				= (tau_Pi>0) && (tau_pi>0) && (eta>0) && (zeta>0)
					&& (tau_pipi>0) && (delta_PiPi>0) && (lambda_Pipi>0)
					&& (delta_pipi>0) && (lambda_piPi>0) && (cs2>0)
					&& (e>0) && (p>=0) && (enthalpy_plus_Pi>0)
					&& (enthalpy_plus_Pi+Lambda_1>0)
					&& (enthalpy_plus_Pi+Lambda_2>0)
					&& (enthalpy_plus_Pi+Lambda_3>0)
					&& (Lambda_1<=0) && (Lambda_3>=0)
					&& (Lambda_1<=Lambda_2) && (Lambda_2<=Lambda_3);

		vector<bool> necessary_conditions(6, false);
		vector<bool> sufficient_conditions(8, false);

		check_necessary_conditions(necessary_conditions);
		check_sufficient_conditions(sufficient_conditions);

		for ( const auto & nc : necessary_conditions ) cout << static_cast<int>( nc );
		cout << "   ";
		for ( const auto & sc : sufficient_conditions ) cout << static_cast<int>( sc );
		cout << "   " << tau << "   " << x << "   " << y << "   "
				<< T << "   " << e << "   "
				<< static_cast<int>(assumptionsSatisfied) << "   "
				<< static_cast<int>(eigenSuccess) << endl;
	}
	else
	{
		test_mode = false;

		// read path to input file from command line
		string path_to_file = string(argv[1]);
	
		// then read in file itself
		ifstream infile(path_to_file.c_str());
		if (infile.is_open())
		{
			string line;
			while ( getline (infile, line) )
			{
				istringstream iss(line);
				iss >> tau >> x >> y
					>> T >> e >> p >> cs2
					>> eta >> zeta >> tau_pi >> tau_Pi
					>> pi00 >> pi01 >> pi02 >> pi11 >> pi12 >> pi22 >> pi33 >> Pi
					>> delta_PiPi >> lambda_Pipi >> delta_pipi >> lambda_piPi
					>> phi_7 >> tau_pipi >> Tr_pi_sigma;
	
				Lambda_0 = 0.0; Lambda_1 = 0.0; Lambda_2 = 0.0; Lambda_3 = 0.0;
				bool eigenSuccess = get_sorted_eigenvalues_of_pi_mu_nu(
									Lambda_0, Lambda_1, Lambda_2, Lambda_3 );

				const double enthalpy_plus_Pi = e+p+Pi;

				bool assumptionsSatisfied
						= (tau_Pi>0) && (tau_pi>0) && (eta>0) && (zeta>0)
							&& (tau_pipi>0) && (delta_PiPi>0) && (lambda_Pipi>0)
							&& (delta_pipi>0) && (lambda_piPi>0) && (cs2>0)
							&& (e>0) && (p>=0) && (enthalpy_plus_Pi>0)
							&& (enthalpy_plus_Pi+Lambda_1>0)
							&& (enthalpy_plus_Pi+Lambda_2>0)
							&& (enthalpy_plus_Pi+Lambda_3>0)
							&& (Lambda_1<=0) && (Lambda_3>=0)
							&& (Lambda_1<=Lambda_2) && (Lambda_2<=Lambda_3);

				if ( !assumptionsSatisfied )
					cerr << "Preconditions violated: "
						 << static_cast<int>(tau_Pi>0)
						 << static_cast<int>(tau_pi>0)
						 << static_cast<int>(eta>0)
						 << static_cast<int>(zeta>0)
						 << static_cast<int>(tau_pipi>0)
						 << static_cast<int>(delta_PiPi>0)
						 << static_cast<int>(lambda_Pipi>0)
						 << static_cast<int>(delta_pipi>0)
						 << static_cast<int>(lambda_piPi>0)
						 << static_cast<int>(cs2>0)
						 << static_cast<int>(e>0)
						 << static_cast<int>(p>=0)
						 << static_cast<int>(enthalpy_plus_Pi>0)	
						 << static_cast<int>(enthalpy_plus_Pi+Lambda_1>0)
						 << static_cast<int>(enthalpy_plus_Pi+Lambda_2>0)
						 << static_cast<int>(enthalpy_plus_Pi+Lambda_3>0)
						 << static_cast<int>(Lambda_1<=0)
						 << static_cast<int>(Lambda_3>=0)
						 << static_cast<int>(Lambda_1<=Lambda_2)
						 << static_cast<int>(Lambda_2<=Lambda_3) << endl;

				vector<bool> necessary_conditions(6, false);
				vector<bool> sufficient_conditions(8, false);

				check_necessary_conditions(necessary_conditions);
				check_sufficient_conditions(sufficient_conditions);

				for ( const auto & nc : necessary_conditions ) cout << static_cast<int>( nc );
				cout << "   ";
				for ( const auto & sc : sufficient_conditions ) cout << static_cast<int>( sc );
				cout << "   " << tau << "   " << x << "   " << y << "   "
						<< T << "   " << e << "   "
						<< static_cast<int>(assumptionsSatisfied) << "   "
						<< static_cast<int>(eigenSuccess) << endl;
			}
		}
	
		infile.close();
	}

	return (0);
}

bool get_sorted_eigenvalues_of_pi_mu_nu(
		double & Lambda_0, double & Lambda_1, double & Lambda_2, double & Lambda_3 )
{
	double m[16];
	m[0]  = -pi00; m[1]  = -pi01; m[2]  = -pi02; m[3]  =  0.0;
	m[4]  =  pi01; m[5]  =  pi11; m[6]  =  pi12; m[7]  =  0.0;
	m[8]  =  pi02; m[9]  =  pi12; m[10] =  pi22; m[11] =  0.0;
	m[12] =  0.0;  m[13] =  0.0;  m[14] =  0.0;  m[15] =  pi33;

	gsl_vector_complex *eval = gsl_vector_complex_alloc(4);
	gsl_matrix_complex *evec = gsl_matrix_complex_alloc(4, 4);

	gsl_matrix_view mat = gsl_matrix_view_array(m, 4, 4);
	gsl_eigen_nonsymmv_workspace *w = gsl_eigen_nonsymmv_alloc(4);
	int success = gsl_eigen_nonsymmv (&mat.matrix, eval, evec, w);
	gsl_eigen_nonsymmv_free(w);

	// sort by magnitude first
	gsl_eigen_nonsymmv_sort(eval, evec, GSL_EIGEN_SORT_ABS_ASC);

	for ( int elem = 0; elem < 4; elem++ )
		if ( abs(GSL_IMAG(gsl_vector_complex_get(eval, elem)))
				> 0.01*abs(GSL_REAL(gsl_vector_complex_get(eval, elem))) )
		{
			cerr << "ERROR(complex): " << -1e100 << " < " << epsilon << ": "
				<< 0.0 << "   " << 0.0 << "   " << 0.0 << "   " << 0.0 << "   ";
			cerr << pi00 << "   " << pi01 << "   " << pi02 << "   "
				<< pi11 << "   " << pi12 << "   " << pi22 << "   " << pi33 << endl;
			return false;
		}

	Lambda_0 = GSL_REAL(gsl_vector_complex_get(eval, 0));
	double ratio = abs(Lambda_0 / (abs(GSL_REAL(gsl_vector_complex_get(eval, 3)))+epsilon));

	/*cout << "Check #1 here: "
		<< GSL_REAL(gsl_vector_complex_get(eval, 0)) << "   "
		<< GSL_REAL(gsl_vector_complex_get(eval, 1)) << "   "
		<< GSL_REAL(gsl_vector_complex_get(eval, 2)) << "   "
		<< GSL_REAL(gsl_vector_complex_get(eval, 3)) << endl;*/

	// sort by value next
	gsl_eigen_nonsymmv_sort(eval, evec, GSL_EIGEN_SORT_VAL_ASC);

	/*cout << "Check #2 here: "
		<< GSL_REAL(gsl_vector_complex_get(eval, 0)) << "   "
		<< GSL_REAL(gsl_vector_complex_get(eval, 1)) << "   "
		<< GSL_REAL(gsl_vector_complex_get(eval, 2)) << "   "
		<< GSL_REAL(gsl_vector_complex_get(eval, 3)) << endl;*/

	double tmp0 = GSL_REAL(gsl_vector_complex_get(eval, 0));
	double tmp1 = GSL_REAL(gsl_vector_complex_get(eval, 1));
	double tmp2 = GSL_REAL(gsl_vector_complex_get(eval, 2));
	double tmp3 = GSL_REAL(gsl_vector_complex_get(eval, 3));


	// sort eval by values
	//Lambda_0 = 0.0;
	Lambda_1 = tmp0;
	Lambda_2 = ( abs(tmp1) > abs(tmp2) ) ? tmp1 : tmp2;
	Lambda_3 = tmp3;

	if ( ratio > 0.01 )
	{
		cerr /*<< "ERROR: no zero eigenvalues found!  " << endl*/
			<< "ERROR: " << ratio << " > " << 0.01 << ": " /*<< endl*/
			<< tmp0 << "   " << tmp1 << "   " << tmp2 << "   " << tmp3 << "   ";
		cerr << pi00 << "   " << pi01 << "   " << pi02 << "   "
			<< pi11 << "   " << pi12 << "   " << pi22 << "   " << pi33 << endl;
		success++;
	}
	//else
	//	cerr << "Found zero eigenvalue with ratio = " << ratio << endl;

	gsl_vector_complex_free(eval);
	gsl_matrix_complex_free(evec);

	return ( success == 0 );
}


// End of file
