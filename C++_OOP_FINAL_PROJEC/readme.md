
Student grade manager-project -report

1.Task description

The goal of this project was to build the a C ++ program that manages a student’s grades .The system calculate grade metrics such as mean ,max, and min using dynamic memory allocation and object-oriented programming. 

- Define a struct `Student` with a name, a dynamically allocated float array for grades, and a count of the number of grades.
- 
- Create an abstract class `GradeMetric` with a pure virtual function `compute(const Student*) = 0`.
- 
- Derive `MeanMetric`, `MaxMetric`, and `MinMetric` classes from `GradeMetric`.
- 
- Store metric objects in a dynamic array of `GradeMetric*` and use polymorphism to compute results.
- 
- Use pointer arithmetic to iterate through the grades array.
- 
- Implement `addGrade(Student&, float)` and `removeGrade(Student&, int)` functions to modify the grade list dynamically
- 
How it was completed

1.A student structure was created to hold the name and dynamic array of grades.
2.An abstract class GradeMetric was defined and extended by three metric classes.
3.Each metric class implementCompute() method using pointer arithmetic
4. A dynamic array of GradeMetric* was used in the main function to store and invoke each metric.
5. Helper function addGrade and removeGrade were used to modify the grades array dynamically.
6. Memory cleanup was carefully handled using destructors and delete() operations

3. annotated code with comments 


Below is the annotated code with explanation for each important line:

1. #include <iostream> // includes input and output stream library


2. #include <cstring> // Includes C-style string handling functions

3. using namespace std; // Avoids needing to prefix std:: everywhere

4. struct Student {// Defines a structure to store student data

5. char name[30]; // Stores the student's name

6. float* grades; // Pointer to dynamically allocated array of grades

7. int nGrades; // Number of grades

8. Student() { // Constructor initializes values

9. grades = nullptr; // Initialize pointer to null

10. nGrades = 0; // Start with 0 grades

11. } // End constructor

12. ~Student() { // Destructor to release memory

13. delete[] grades; // Delete dynamically allocated grades

14. } // End destructor

15. }; // End of Student struct

16. class GradeMetric { // Abstract base class for metrics

public: 
17. virtual float compute(const Student* s) = 0; // Pure virtual function for computing metric

18. virtual const char* name() const = 0; // Returns metric name

19. virtual ~GradeMetric() {} // Virtual destructor

20. }; // End GradeMetric class

30. class MeanMetric : public GradeMetric { // Derived class to compute mean

public: 
31. float compute(const Student* s) override { // Override compute function


32. float sum = 0; // Initialize sum

33. for (int i = 0; i < s->nGrades; i++) { // Loop over grades

34. sum += *(s->grades + i); // Add grade using pointer arithmetic
} 
35. return sum / s->nGrades; // Return mean value
} 
36. const char* name() const override { return "Mean"; } // Return metric name

37. }; // End MeanMetric

// Similar classes: MaxMetric and MinMetric (omitted for brevity) 
38. void addGrade(Student& s, float grade) { // Adds a grade by reallocating memory

39. float* newGrades = new float[s.nGrades + 1]; // Allocate new larger array

40. for (int i = 0; i < s.nGrades; i++) // Copy old grades

41. *(newGrades + i) = *(s.grades + i); // Use pointer arithmetic

42. *(newGrades + s.nGrades) = grade; // Add new grade

43. delete[] s.grades; // Free old array

44. s.grades = newGrades; // Assign new array

45. s.nGrades++; // Increment number of grades

46. } // End addGrade

47. void removeGrade(Student& s, int index) { // Removes grade at specified index

48. if (index < 0 || index >= s.nGrades) return; // Check bounds

49. float* newGrades = new float[s.nGrades - 1]; // Allocate smaller array

50. for (int i = 0, j = 0; i < s.nGrades; i++) { // Loop and skip index

51. if (i != index) *(newGrades + j++) = *(s.grades + i); // Copy except removed
} 
52. delete[] s.grades; // Free old memory

53. s.grades = newGrades; // Assign new array

54. s.nGrades--; // Decrease grade count

} // End removeGrade

55. int main() { // Start of main function

56. Student s; // Create student object

57. cin.getline(s.name, 30); // Input student name

58. int n; cin >> n; // Input number of grades

59. for (int i = 0; i < n; i++) { // Loop for grades

60. float g; cin >> g; addGrade(s, g); // Input and add grade

} 
61. GradeMetric* metrics[3] = { new MeanMetric(), new MaxMetric(), new MinMetric() }; // Create metrics

62. for (int i = 0; i < 3; i++) { // Display results

63. cout << metrics[i]->name() << ": " << metrics[i]->compute(&s) << endl; // Call polymorphic compute

64. delete metrics[i]; // Free metric
} 
65. return 0; // End program
} // End main

SCREEN SHOOT


![Screenshot 6](https://github.com/user-attachments/assets/f0f81fbc-a4dd-4e73-a508-304e411d8324)
![Screenshot 5](https://github.com/user-attachments/assets/dc13367f-cefc-496c-ade1-4695744c6541)
![Screenshot 4](https://github.com/user-attachments/assets/971d95db-744a-4be8-870a-ac53480524ea)
![Screenshot 3](https://github.com/user-attachments/assets/ea52081a-e45c-410f-9e17-10fe5c72eccc)
![Screenshot 2](https://github.com/user-attachments/assets/fdc4c42d-20cc-4280-a81d-b1ed2c230194)

![Screenshot 1](https://github.com/user-attachments/assets/1ec7ec59-b235-4fc7-8895-892c4a00455d)






