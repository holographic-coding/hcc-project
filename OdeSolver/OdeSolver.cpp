#include <iostream>
#include <fstream>
using namespace std;


int main() {

//Leemos la matriz de condiciones iniciales
    int Init[7][2];
    int i;
    int j;
    ifstream fileInit("initial/initial.dat");
    ofstream fileOut("results/results.dat",ios::out); //Crea el fichero de salida

    if (fileInit.is_open()){
        for (i=0;i<7;i++){
            for (j=0;j<2;j++){        
                if(fileInit.good()){
                    fileInit >> Init[i][j];
                    }
             }
          }
       }
    else cout << "No es posible abrir el archivo." << endl;
  
// Imprimimos en pantalla la matriz
  for( int i=0; i<7; i++){
    for (int j=0; j<2; j++){
        cout <<Init[i][j]<< ((j+1) % 2 ? " ": "\n");
    }
  }

//Guardamos la matriz en el fichero results.dat en el directorio results.


    if (fileOut.is_open()){
        for (i=0;i<7;i++){
            for (j=0;j<2;j++){        
                fileOut <<Init[i][j]<< ((j+1) % 2 ? " ": "\n");
              }
          }
       }


    return 0;
}

