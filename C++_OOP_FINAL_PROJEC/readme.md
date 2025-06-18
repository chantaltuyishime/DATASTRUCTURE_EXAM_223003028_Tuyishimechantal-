
Student grade manager-project -report 
1.Task description
The goal of this project was to build the a C ++ program that manages a student’s grades .The system calculate grade metrics such as mean ,max, and min using dynamic memory allocation and object-oriented programming. 
- Define a struct `Student` with a name, a dynamically allocated float array for grades, and a count of the number of grades.
- Create an abstract class `GradeMetric` with a pure virtual function `compute(const Student*) = 0`.
- Derive `MeanMetric`, `MaxMetric`, and `MinMetric` classes from `GradeMetric`.
- Store metric objects in a dynamic array of `GradeMetric*` and use polymorphism to compute results.
- Use pointer arithmetic to iterate through the grades array.
- Implement `addGrade(Student&, float)` and `removeGrade(Student&, int)` functions to modify the grade list dynamically
How it was completed 
1.A student structure was created to hold the name and dynamic array of grades.
2.An abstract class GradeMetric was defined and extended by three metric classes.
3.Each metric class implementCompute() method using pointer arithmetic
4. A dynamic array of GradeMetric* was used in the main function to store and invoke each metric.
5. Helper function addGrade and removeGrade were used to modify the grades array dynamically.
6. Memory cleanup was carefully handled using destructors and delete() operations.
3. annotated code with comments 
Below is the annotated code with explanation for each important line:
#include <iostream> // includes input and output stream library 
#include <cstring> // Includes C-style string handling functions
using namespace std; // Avoids needing to prefix std:: everywhere
struct Student {// Defines a structure to store student data
char name[30]; // Stores the student's name
float* grades; // Pointer to dynamically allocated array of grades
int nGrades; // Number of grades
Student() { // Constructor initializes values
grades = nullptr; // Initialize pointer to null
nGrades = 0; // Start with 0 grades
} // End constructor
~Student() { // Destructor to release memory
delete[] grades; // Delete dynamically allocated grades
} // End destructor
}; // End of Student struct
class GradeMetric { // Abstract base class for metrics
public: 
virtual float compute(const Student* s) = 0; // Pure virtual function for computing metric
virtual const char* name() const = 0; // Returns metric name
virtual ~GradeMetric() {} // Virtual destructor
}; // End GradeMetric class
class MeanMetric : public GradeMetric { // Derived class to compute mean
public: 
float compute(const Student* s) override { // Override compute function
float sum = 0; // Initialize sum
for (int i = 0; i < s->nGrades; i++) { // Loop over grades
sum += *(s->grades + i); // Add grade using pointer arithmetic
} 
return sum / s->nGrades; // Return mean value
} 
const char* name() const override { return "Mean"; } // Return metric name
}; // End MeanMetric
// Similar classes: MaxMetric and MinMetric (omitted for brevity) 
void addGrade(Student& s, float grade) { // Adds a grade by reallocating memory
float* newGrades = new float[s.nGrades + 1]; // Allocate new larger array
for (int i = 0; i < s.nGrades; i++) // Copy old grades
*(newGrades + i) = *(s.grades + i); // Use pointer arithmetic
*(newGrades + s.nGrades) = grade; // Add new grade
delete[] s.grades; // Free old array
s.grades = newGrades; // Assign new array
s.nGrades++; // Increment number of grades
} // End addGrade
void removeGrade(Student& s, int index) { // Removes grade at specified index
if (index < 0 || index >= s.nGrades) return; // Check bounds
float* newGrades = new float[s.nGrades - 1]; // Allocate smaller array
for (int i = 0, j = 0; i < s.nGrades; i++) { // Loop and skip index
if (i != index) *(newGrades + j++) = *(s.grades + i); // Copy except removed
} 
delete[] s.grades; // Free old memory
s.grades = newGrades; // Assign new array
s.nGrades--; // Decrease grade count
} // End removeGrade
int main() { // Start of main function
Student s; // Create student object
cin.getline(s.name, 30); // Input student name
int n; cin >> n; // Input number of grades
for (int i = 0; i < n; i++) { // Loop for grades
float g; cin >> g; addGrade(s, g); // Input and add grade
} 
GradeMetric* metrics[3] = { new MeanMetric(), new MaxMetric(), new MinMetric() }; // Create metrics
for (int i = 0; i < 3; i++) { // Display results
cout << metrics[i]->name() << ": " << metrics[i]->compute(&s) << endl; // Call polymorphic compute
delete metrics[i]; // Free metric
} 
return 0; // End program
} // End main

SCREEN SHOOT


![Screenshot 6](https://github.com/user-attachments/assets/f0f81fbc-a4dd-4e73-a508-304e411d8324)
![Screenshot 5](https://github.com/user-attachments/assets/dc13367f-cefc-496c-ade1-4695744c6541)
![Screenshot 4](https://github.com/user-attachments/assets/971d95db-744a-4be8-870a-ac53480524ea)
![Screenshot 3](https://github.com/user-attachments/assets/ea52081a-e45c-410f-9e17-10fe5c72eccc)
![Screenshot 2](https://github.com/user-attachments/assets/fdc4c42d-20cc-4280-a81d-b1ed2c230194)

![Screenshot 1](https://github.com/user-attachments/assets/1ec7ec59-b235-4fc7-8895-892c4a00455d)






