#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

// Returns true if triangle is possible
bool possible_triangle(vector<int> sides)
{
    bool possible = true;

    // Check if any one side of larger or equal to the other two
    // if so the triangle is impossible
    for (int side : sides)
    {
        vector<int> other_sides;
        other_sides = sides;
        auto cur_side = find(other_sides.begin(),other_sides.end(),side);
        other_sides.erase(cur_side);

        if (side >= other_sides[0] + other_sides[1])
        {
            possible = false;
            break;
        }
    }

    return possible;
}


int main()
{
    // Read the input file
    ifstream fs("input.txt");
    string triangle_spec;

    int possible_triangles = 0;

    while (getline(fs, triangle_spec))
    {
        // Triangle according to spec is possible
        bool possible;

        // Create a string stream from the spec for a single triangle
        stringstream s(triangle_spec);

        // Create vector of sides
        vector<int> sides;
        int side;
        while (s >> side)
        {
            sides.push_back(side);
        }

        // Check if triangle is possible
        possible = possible_triangle(sides);

        if (possible)
        {
            possible_triangles += 1;
        }
    }
    cout << "Possible triangles: " << possible_triangles << endl;
    return 0;
}
