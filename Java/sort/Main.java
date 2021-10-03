
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.FileNotFoundException;
import java.util.*;
import java.io.*;
import java.io.File;
import java.util.Scanner;

import java.io.FileReader;

public class Main
{

    void generar(int[] a,int tam)
    {
        FileWriter fichero = null;
		try {

			fichero = new FileWriter("generarNumeros.txt");

			// Escribimos linea a linea en el fichero
			for (int i=0;i<tam;i++) {
                int numero = (int)(Math.random()*100+1);
				fichero.write(numero + "\n");
			}

			fichero.close();

		} catch (Exception ex) {
			System.out.println("Mensaje de la excepción: " + ex.getMessage());
		}
        

        String[] nombre=new String[tam];
        BufferedReader fr = null;
        try {
            //Abrir el fichero indicado en la variable nombreFichero
            fr = new BufferedReader(new FileReader("generarNumeros.txt"));
            //Leer el primer carácter
            //Se debe almacenar en una variable de tipo int
            String caract = fr.readLine();
            int i=0;
            //Se recorre el fichero hasta encontrar el carácter -1
            //   que marca el final del fichero
            while(caract != null) {
                //Mostrar en pantalla el carácter leído convertido a char

                String linea=caract;
                nombre[i]=linea;
                i=i+1;
                //Leer el siguiente carácter
                caract = fr.readLine();
            }
        }
        catch (FileNotFoundException e) {
            //Operaciones en caso de no encontrar el fichero
            System.out.println("Error: Fichero no encontrado");
            //Mostrar el error producido por la excepción
            System.out.println(e.getMessage());
        }
        catch (Exception e) {
            //Operaciones en caso de error general
            System.out.println("Error de lectura del fichero");
            System.out.println(e.getMessage());
        }
        finally {
            //Operaciones que se harán en cualquier caso. Si hay error o no.
            try {
                //Cerrar el fichero si se ha abierto
                if(fr != null)
                    fr.close();
            }
            catch (Exception e) {
                System.out.println("Error al cerrar el fichero");
                System.out.println(e.getMessage());
            }
        }


        
        for(int i=0;i<nombre.length ;i++)
        {
            if(nombre[i]!=null)
                a[i] = Integer.parseInt(nombre[i]); 
        }

    }

    void printArray(int a[])
    {
        for(int i=0;i<a.length ;i++)
        { 
            System.out.println(a[i]+ " ");
        } 
    }

    public static void main(String[] args)
    {
        BubbleSort bs = new BubbleSort();
        InsertionSort is = new InsertionSort();
        HeapSort hs=new HeapSort();
        MergeSort ms=new MergeSort();
        SelectionSort ss=new SelectionSort();
        ShellSort shs=new ShellSort();
        QuickSort qs=new QuickSort();
        Main m=new Main();


        
        
        FileWriter burbuja=null;
        FileWriter heapsort=null;
        FileWriter insertionsort=null;
        FileWriter selectionsort=null;
        FileWriter shellsort=null;
        FileWriter mergesort=null;
        FileWriter quicksort=null;
        
        /* BURBUJA */
        try {

            burbuja = new FileWriter("../tiempos/burbuja_tiempo_java.txt");

            int n;
            for(int i=1;i<21;i++)
            {
                n=i*5000;
                System.out.println(n);

                int[] arr=new int[n];
                m.generar(arr, n);
                long inicio = System.currentTimeMillis();
                bs.bubbleSort(arr);
                long fin = System.currentTimeMillis();
                double tiempo =  ((fin - inicio)/1000);
                burbuja.write(n + "," + tiempo +"\n");
                arr=null; 


            }
            burbuja.close();

        } catch (Exception ex) {
            System.out.println("Mensaje de la excepción: " + ex.getMessage());
        }




        /* HEAPSORT */

        try {

            heapsort = new FileWriter("../tiempos/heapsort_tiempo_java.txt");
            

            int n;
            for(int i=1;i<21;i++)
            {
                n=i*5000;
                System.out.println(n);

                int[] arr2=new int[n];
                m.generar(arr2, n);
                long inicio2 = System.currentTimeMillis();
                hs.sort(arr2);
                long fin2 = System.currentTimeMillis();
                double tiempo2 =  ((fin2 - inicio2)/1000);
                heapsort.write(n + "," + tiempo2 +"\n");
                arr2=null; 


            }
            heapsort.close();

        } catch (Exception ex) {
            System.out.println("Mensaje de la excepción: " + ex.getMessage());
        }
        /* INSERTIONSORT */

        try {

            insertionsort = new FileWriter("../tiempos/insertion_tiempo_java.txt");
            

            int n;
            for(int i=1;i<21;i++)
            {
                n=i*5000;
                System.out.println(n);
                int[] arr3=new int[n];
                m.generar(arr3, n);
                long inicio3 = System.currentTimeMillis();
                is.insertionSort(arr3);
                long fin3 = System.currentTimeMillis();
                double tiempo3 =  ((fin3 - inicio3)/1000);
                insertionsort.write(n + "," + tiempo3 +"\n");
                arr3=null; 



            }
            insertionsort.close();

        } catch (Exception ex) {
            System.out.println("Mensaje de la excepción: " + ex.getMessage());
        }

        /* SELECTIONSORT */

        try {

            selectionsort = new FileWriter("../tiempos/selection_tiempo_java.txt");


            int n;
            for(int i=1;i<21;i++)
            {
                n=i*5000;
                System.out.println(n);


                int[] arr4=new int[n];
                m.generar(arr4, n);
                long inicio4 = System.currentTimeMillis();
                ss.selectionSort(arr4);
                long fin4 = System.currentTimeMillis();
                double tiempo4 =  ((fin4 - inicio4)/1000);
                selectionsort.write(n + "," + tiempo4 +"\n");
                arr4=null; 


            }
            selectionsort.close();

        } catch (Exception ex) {
            System.out.println("Mensaje de la excepción: " + ex.getMessage());
        }

        /* SHELLSORT */

        try {
            shellsort = new FileWriter("../tiempos/shellsort_tiempo_java.txt");
            int n;
            for(int i=1;i<21;i++)
            {
                n=i*5000;
                System.out.println(n);

                 int[] arr5=new int[n];
                m.generar(arr5, n);
                long inicio5 = System.currentTimeMillis();
                shs.shellSort(arr5);
                long fin5 = System.currentTimeMillis();
                double tiempo5 =  ((fin5 - inicio5)/1000);
                shellsort.write(n + "," + tiempo5 +"\n");
                arr5=null; 

            }
            shellsort.close();

        } catch (Exception ex) {
            System.out.println("Mensaje de la excepción: " + ex.getMessage());
        }
        /* MERGESORT */

        try {

            mergesort = new FileWriter("../tiempos/mergesort_tiempo_java.txt");

            int n;
            for(int i=1;i<21;i++)
            {
                n=i*5000;
                System.out.println(n);

                int[] arr6=new int[n];
                m.generar(arr6, n);
                long inicio6 = System.currentTimeMillis();
                ms.mergeSort(arr6, 0, arr6.length-1);
                long fin6 = System.currentTimeMillis();
                double tiempo6 =  ((fin6 - inicio6)/1000);
                mergesort.write(n + "," + tiempo6 +"\n");
                arr6=null;
            

            }
            mergesort.close();

        } catch (Exception ex) {
            System.out.println("Mensaje de la excepción: " + ex.getMessage());
        }

        /* QUICKSORT */

        try {

            quicksort = new FileWriter("../tiempos/quicksort_tiempo_java.txt");

            int n;
            for(int i=1;i<21;i++)
            {
                n=i*5000;
                System.out.println(n);

                int[] arr7=new int[n];
                m.generar(arr7, n);
                long inicio7 = System.currentTimeMillis();
                qs.quickSort(arr7, 0, arr7.length-1);
                long fin7 = System.currentTimeMillis();
                double tiempo7 =  ((fin7 - inicio7)/1000);
                quicksort.write(n + "," + tiempo7 +"\n");
                arr7=null; 


            }
            quicksort.close();

        } catch (Exception ex) {
            System.out.println("Mensaje de la excepción: " + ex.getMessage());
        }

    }
}