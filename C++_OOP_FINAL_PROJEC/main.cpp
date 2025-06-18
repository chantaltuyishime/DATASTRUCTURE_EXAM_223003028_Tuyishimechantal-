#include <iostream>
#include <cstring>
using namespace std;

// STRUCT: Student
struct Student {
    char name[30];
    float* grades;
    int nGrades;

    Student() {
        grades = nullptr;
        nGrades = 0;
    }

    ~Student() {
        delete[] grades;
    }
};

// ABSTRACT CLASS: GradeMetric
class GradeMetric {
public:
    virtual float compute(const Student* s) = 0;
    virtual const char* name() const = 0;
    virtual ~GradeMetric() {}
};

// DERIVED CLASS: MeanMetric
class MeanMetric : public GradeMetric {
public:
    float compute(const Student* s) override {
        if (s->nGrades == 0) return 0;
        float sum = 0;
        for (int i = 0; i < s->nGrades; i++) {
            sum += *(s->grades + i); // pointer arithmetic
        }
        return sum / s->nGrades;
    }

    const char* name() const override {
        return "Mean";
    }
};

// DERIVED CLASS: MaxMetric
class MaxMetric : public GradeMetric {
public:
    float compute(const Student* s) override {
        if (s->nGrades == 0) return 0;
        float max = *(s->grades);
        for (int i = 1; i < s->nGrades; i++) {
            if (*(s->grades + i) > max)
                max = *(s->grades + i);
        }
        return max;
    }

    const char* name() const override {
        return "Max";
    }
};

// DERIVED CLASS: MinMetric
class MinMetric : public GradeMetric {
public:
    float compute(const Student* s) override {
        if (s->nGrades == 0) return 0;
        float min = *(s->grades);
        for (int i = 1; i < s->nGrades; i++) {
            if (*(s->grades + i) < min)
                min = *(s->grades + i);
        }
        return min;
    }

    const char* name() const override {
        return "Min";
    }
};

// FUNCTION: Add Grade to Student
void addGrade(Student& s, float grade) {
    float* newGrades = new float[s.nGrades + 1];
    for (int i = 0; i < s.nGrades; i++) {
        *(newGrades + i) = *(s.grades + i);
    }
    *(newGrades + s.nGrades) = grade;
    delete[] s.grades;
    s.grades = newGrades;
    s.nGrades++;
}

int main() {
    Student s;
    cout << "=== STUDENT GRADE MANAGER ===\n\n";

    cout << "Step 1: Enter student name: ";
    cin.getline(s.name, 30);

    int n;
    cout << "\nStep 2: How many grades to input? ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        float g;
        cout << "Enter grade #" << (i + 1) << ": ";
        cin >> g;
        addGrade(s, g);
    }

    // Initialize metrics
    GradeMetric* metrics[3];
    metrics[0] = new MeanMetric();
    metrics[1] = new MaxMetric();
    metrics[2] = new MinMetric();

    // Menu
    int choice;
    do {
        cout << "\n--- Select an Option ---\n";
        cout << "1. Show Mean\n";
        cout << "2. Show Min\n";
        cout << "3. Show Max\n";
        cout << "4. Show All\n";
        cout << "0. Exit\n";
        cout << "Choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Mean: " << metrics[0]->compute(&s) << endl;
                break;
            case 2:
                cout << "Min: " << metrics[2]->compute(&s) << endl;
                break;
            case 3:
                cout << "Max: " << metrics[1]->compute(&s) << endl;
                break;
            case 4:
                cout << "\n--- Grade Report for " << s.name << " ---\n";
                for (int i = 0; i < 3; i++) {
                    cout << metrics[i]->name() << ": " << metrics[i]->compute(&s) << endl;
                }
                break;
            case 0:
                break;
            default:
                cout << "Invalid option.\n";
        }

    } while (choice != 0);

    // Clean up
    for (int i = 0; i < 3; i++) {
        delete metrics[i];
    }

    cout << "\n=== END OF PROGRAM ===\n";
    return 0;
}
