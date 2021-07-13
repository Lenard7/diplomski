#include <iostream>
#include <fstream>
#include <string>

int main()
{
    std::string gainLine;
	std::ofstream gainFileWrite;
    gainFileWrite.open("gainFile.txt", std::ofstream::app);
		
	//writing to file
	gainFileWrite << "pero";//Gain_of_candidate;
    gainFileWrite << "\n";

	//reading from file
	std::ifstream gainFileRead("gainFile.txt");

	while (std::getline(gainFileRead, gainLine)) {
       	std::cout << gainLine << "\n";
    }

    gainFileRead.close();
	
	gainFileWrite.close();

    return 0;
}