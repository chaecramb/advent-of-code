#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <algorithm>
#include <fstream>

using namespace std;


// Turn left or right and return new orientation
int Turn (char direction, int current_orientation)
{
    // This looks ugly but accounts for the fact that modulo in C/C++ is really
    // rem rather than mod, so won't return the intended result for negatives.
    // TODO: refactor to a clearer solution
    if (direction == 'L') {
        return (((current_orientation - 1) % 4) + 4) % 4;
    } else {
        return (((current_orientation + 1) % 4) + 4) % 4;
    }
}


// Parse input and convert to vector pathway
vector<string> GetPathway (string input)
{
    vector<string> pathway;
    stringstream ss(input);
    string step;

    while(getline(ss, step, ',')) {
        ss.ignore();
        pathway.push_back(step);
    }
    return pathway;
}


void PrintResult(int distance)
{
    cout << "Shortest distance is: "
         << distance
         << endl;
}


// Constant relating orientation to movements
map<int, pair<int, int>> kMovements = {
                                {0, {0,1}},
                                {1, {1,0}},
                                {2, {0,-1}},
                                {3, {-1,0}}
                              };


int main()
{
    // Read the input file and convert to a string
    ifstream ifs("input.txt");
    string input( (istreambuf_iterator<char>(ifs) ),
                 (istreambuf_iterator<char>()    ) );

    // Initial orientation, 0 = north, 1 = east, 2 = south, 3 = west
    int orientation = 0;

    // Initial position
    pair <int, int> position (0,0);

    // Route vector to keep track of locations visited
    vector<pair<int, int>> route;

    // Get pathway vector from input
    vector<string> pathway = GetPathway(input);

    // Iteratre through the pathway
    for (string step : pathway) {
        // Get direction and distance from the step
        char direction = step[0];
        int distance = stoi(step.substr(1));

        // Turn to face a new orientation
        orientation = Turn(direction, orientation);

        // Calculate movements
        int horizontal_move = kMovements[orientation].first;
        int vertical_move = kMovements[orientation].second;

        // Move distance steps in new orientation
        // appending each new poistion to route
        for (int i = 0; i < distance; ++i) {
            position.first += horizontal_move;
            position.second += vertical_move;

            // Return early if position has already been visited
            if(find(route.begin(), route.end(), position) != route.end()) {
                PrintResult(abs(position.first) + abs(position.second));
                return 0;
            }

            // Add current position to route
            route.push_back(position);
        }
    }

    PrintResult(abs(route.back().first) + abs(route.back().second));

    return 0;
}
