import java.util.*;

public class InsertionSort{

    public static insertion_sort(int[] a){
        // array length
        int n = a.length;
        // CLRS Merge Sort Algorithm Skeleton modified for Java
        int n = array.length;
        for (int j = 1; j < n; j++) {
            int key = array[j];
            int i = j-1;
            while ( (i > -1) && ( array [i] > key ) ) {
                array [i+1] = array [i];
                i--;
            }
            array[i+1] = key;
        }
    }

    public static void main(String[] args) {
        int[] a = [567, 39, 56, 29, 10, 6, 2, 8, 47, 4806, 100, 55, 276];
        long start = System.nanoTime();

    }
}