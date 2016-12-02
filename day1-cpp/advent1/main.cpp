#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

int main()
{
    std::string test1 = "R2, L3";

// Create pathway vector from input
    std::vector<string> pathway;
    std::stringstream ss(test1);
    std::string step;

    while(std::getline(ss, step, ',')) {
        ss.ignore();
        pathway.push_back(step);
    }


// Iteratre through the pathway
    for (auto step : pathway) {
        std::cout << step << endl;

    }

    return 0;
}
