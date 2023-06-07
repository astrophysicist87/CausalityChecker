#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
  if (argc < 3)
  {
    cout << "<<<=========================================================>>>" << endl;
    cout << "Usage: ./get_light_cone_data /path/to/causality_check_file"
            " /path/to/local_speed_file" << endl;
    cout << "<<<=========================================================>>>" << endl;
    std::terminate();
  }

  string causality_check_path = argv[1];
  string local_speed_path     = argv[2];

  ifstream infile_CC(causality_check_path.c_str());
  ifstream infile_LS(causality_check_path.c_str());
  if (infile_CC.is_open() && infile_LS.is_open())
  {
    const int CC_fields_to_skip = 9;
    double dummy, tau, x, y, v;
    string lineCC, lineLS;
    while ( getline(infile_CC, lineCC) && getline(infile_LS, lineLS) )
    {
      // convert this line to fields
      istringstream issCC(lineCC);
      istringstream issLS(lineLS);

      // skip prescribed number of fields
      for (int field = 0; field < CC_fields_to_skip; ++field) issCC >> dummy;

      // get characteristic velocities
      vector<double> characteristic_velocities;
      while (issCC >> dummy) characteristic_velocities.push_back( dummy );
      auto it = max_element( std::begin(characteristic_velocities),
                             std::end(characteristic_velocities) );
      double max_cv = *it;

      // read all fields from local speed file
      issLS >> tau >> x >> y >> v;

      cout << "CHECK:";
      for (auto cv: characteristic_velocities) cout << "  " << cv;
      cout << "\n\n";

      cout << tau << "  " << x << "  " << y << "  " << v << "  " << max_cv << "\n";
      std::terminate();
    }
  }

  return 0;
}
