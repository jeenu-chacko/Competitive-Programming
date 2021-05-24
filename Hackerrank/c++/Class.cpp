#include <iostream>
#include <sstream>
using namespace std;

class Student{
    
  private:
    int age;
    string first_name;
    string last_name;
    int standard;
    
  public:
  void set_first_name(string afirst_name){
      first_name=afirst_name;
  }
  void set_last_name(string alast_name){
     last_name=alast_name;
  }
  
  void set_age(int aage)
  {
      age=aage;
  }
  void set_standard(int astandard) 
  {
      standard= astandard;
  }
  
  string get_first_name()
  {
      return first_name;
  }
  
  string get_last_name()
  {
      return last_name;
  }
  
  int get_age()
  {
      return age;
  }
  
  int get_standard()
  {
      return standard;
  }
  
   string to_string()
    {
        stringstream ss;
        char c = ',';
        ss << age << c << first_name << c << last_name << c << standard;
        return ss.str();
    }
};

int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}

