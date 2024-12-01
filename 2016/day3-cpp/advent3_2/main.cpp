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
    int side;
    vector<vector<int>> triangles = {{}, {}, {}};

    int possible_triangles = 0;

    int num_cols = 3;

    // Iterate through the sides filestream.
    // Check 3 rows at a time in order to capture all sides of each triangle
    // 3 rows equates to 3 * num_cols sides
    int side_count = 0; // sides processed in the current 3 rows
    while (fs >> side)
    {
        triangles.at(side_count % num_cols).push_back(side);

        // Check if we've completed 3 rows
        if (side_count == num_cols * 3 - 1)
        {
            // Loop through triangles by references
            for (auto& triangle : triangles)
            {
                if (possible_triangle(triangle))
                    possible_triangles += 1;
                triangle.clear();
            }
            // Reset i before moving on to the next row
            side_count = -1;
        }
        // Increment the number of sides processed for the current 3 row group
        ++side_count;
    }
    cout << "Possible triangles: " << possible_triangles << endl;
    return 0;
}
