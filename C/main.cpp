#include <stdlib.h>
#include <iostream>
#include <bits/stdc++.h>
#include <fstream>

#include "bubble_sort.cpp"
#include "heap_sort.cpp"
#include "insertion_sort.cpp"
#include "selection_sort.cpp"
#include "shell_sort.cpp"
#include "merge_sort.cpp"
#include "quick_sort.cpp"

using namespace std;

int* generar(int n){
    int num;
    int* array = new int[n];
    srand (time(NULL));

    for (int i = 0; i < n; i++){
        num = rand() % n + 1;
        array[i] = num;
    }

    return array;
}

void mostrar(int* array, int n){
    for (int i = 0; i < n; i++){
        cout<<array[i]<<" ";
    }
    cout<<endl;
}

int* copy(int* array1, int n){
    int* array2 = new int[n];
    for (int i = 0; i < n; i++){
        array2[i] = array1[i];
    }
    return array2;
}

int main(){
    int n = 1000;
    int* array2;
    clock_t start, end;
    ofstream burbuja,heapsort,insertionsort,selectionsort,shellsort,mergesort,quicksort;
    double elapsed;
    burbuja.open("./tiempos/burbuja_tiempo_c++.txt");
    heapsort.open("./tiempos/heapsort_tiempo_c++.txt");
    insertionsort.open("./tiempos/insertionsort_tiempo_c++.txt");
    selectionsort.open("./tiempos/selectionsort_tiempo_c++.txt");
    shellsort.open("./tiempos/shellsort_tiempo_c++.txt");
    mergesort.open("./tiempos/mergesort_tiempo_c++.txt");
    quicksort.open("./tiempos/quicksort_tiempo_c++.txt");

    for(int i=1;i<=20;i++){
        n = 5000*i;
        int* array1 = generar(n);

        //Bubble sort
        array2 = copy(array1, n);
        start = clock();
        bubbleSort(array2,n);
        end = clock();
        elapsed = double(end - start)/double(CLOCKS_PER_SEC);
        burbuja<<n<<" , "<<elapsed<<"\n";
        free(array1);
    }
    for(int i=1;i<=20;i++){
        n = 5000*i;
        int* array1 = generar(n);

        //Heap sort
        array2 = copy(array1, n);
        start = clock();
        heapSort(array2,n);
        end = clock();
        elapsed = double(end - start)/double(CLOCKS_PER_SEC);
        heapsort<<n<<" , "<<elapsed<<"\n";
        free(array1);
    }
    for(int i=1;i<=20;i++){
        n = 5000*i;
        int* array1 = generar(n);

        //Insertion sort
        array2 = copy(array1, n);
        start = clock();
        insertionSort(array2,n);
        end = clock();
        elapsed = double(end - start)/double(CLOCKS_PER_SEC);
        insertionsort<<n<<" , "<<elapsed<<"\n";
        free(array1);
    }
    for(int i=1;i<=20;i++){
        n = 5000*i;
        int* array1 = generar(n);

        //Selection sort
        array2 = copy(array1, n);
        start = clock();
        selectionSort(array2,n);
        end = clock();
        elapsed = double(end - start)/double(CLOCKS_PER_SEC);
        selectionsort<<n<<" , "<<elapsed<<"\n";
        free(array1);
    }
    for(int i=1;i<=20;i++){
        n = 5000*i;
        int* array1 = generar(n);

        //Shell sort
        array2 = copy(array1, n);
        start = clock();
        shellSort(array2,n);
        end = clock();
        elapsed = double(end - start)/double(CLOCKS_PER_SEC);
        shellsort<<n<<" , "<<elapsed<<"\n";

        free(array1);
    }
    for(int i=1;i<=20;i++){
        n = 5000*i;
        int* array1 = generar(n);

        //Merge sort
        array2 = copy(array1, n);
        start = clock();
        mergeSort(array2, 0, n-1);
        end = clock();
        elapsed = double(end - start)/double(CLOCKS_PER_SEC);
        mergesort<<n<<" , "<<elapsed<<"\n";

        free(array1);
    }
    for(int i=1;i<=20;i++){
        n = 5000*i;
        int* array1 = generar(n);

        //Quick sort
        array2 = copy(array1, n);
        start = clock();
        quickSort(array2, 0, n-1);
        end = clock();
        elapsed = double(end - start)/double(CLOCKS_PER_SEC);
        quicksort<<n<<" , "<<elapsed<<"\n";
        free(array1);
    }
    burbuja.close();
    heapsort.close();
    insertionsort.close();
    selectionsort.close();
    shellsort.close();
    mergesort.close();
    quicksort.close();
    return 0;
}