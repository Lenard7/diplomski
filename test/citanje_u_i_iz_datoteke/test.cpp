#include <iostream>
#include <fstream>
#include <string>

/*
ofstream - creates and writes to files
ifstream - reads from files
fstream - ofstream + ifstream
*/

int main()
{
    std::string unesi;
    std::string mytext;
    std::string zavrsi = "gotovo";
    int comp_res;

    std::ofstream MyFile("test.txt");
    do
    {
        // Pisanje u file
        std::cout << "vrijednost za upisati u file" << std::endl;
        std::cout << "uneseni_string = ";
        std::cin >> unesi;   
        MyFile << unesi;
        MyFile << "\n";

        //Citanje iz filea
        std::ifstream MyReadFile("test.txt");

        while (std::getline(MyReadFile, mytext)) {
            std::cout << mytext << "\n";
        }
    
        MyReadFile.close();
    
        comp_res = unesi.compare(zavrsi); 
    } while (comp_res != 0);
    MyFile.close();
    
    return 0;
}