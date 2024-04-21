#include <stdlib.h>
#include <stdio.h>
#include <time.h>

void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    if (left < n && arr[left] > arr[largest]){
        largest = left;
    }
    if (right < n && arr[right] > arr[largest]){
        largest = right;
    }
    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

void buildHeap(int arr[], int n) {
    int startIdx = (n / 2) - 1;
    for (int i = startIdx; i >= 0; i--) {
        heapify(arr, n, i);
    }
}

void heapSort(int arr[], int n) {
    buildHeap(arr, n);
    for (int i = n - 1; i >= 0; i--) {
        swap(&arr[0], &arr[i]);
        heapify(arr, i, 0);
    }
}

void printArray(int arr[], int n) {
    printf("[ ");
    for (int i = 0; i < n; ++i){
        printf("%d ", arr[i]);
    }
    printf("\n");
    printf(" ]\n");
}


int main() {
    clock_t t1,t2;
    t1 = clock();

    double execTime;
    int n = 100;
    int ar[n];
    srand(42);

    for (int i; i<n; i++){
        ar[i] = rand() % 100;
    }

    printf("RandomlyGenerated Array: \n");
    printArray(ar, n);

    heapSort(ar, n);
    printf("HeapSorted array: \n");
    printArray(ar, n);
    t2 = clock();

    execTime = ((double) (t2-t1) / CLOCKS_PER_SEC);
    printf("execTime: %f Secs", execTime);
    return 0;
}
