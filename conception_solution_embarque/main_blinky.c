/*
Author: Jérémie LAERA
State: code can be run with a classic c main() function
       but is not implemented using FreeRTOS tasks and subroutines 
*/

#include <stdio.h>
#include <stdlib.h>  
#include "FreeRTOS.h"
#include "task.h"
#include <time.h>

#define ARRAY_SIZE (1 << 10)   // limit to 2^10 for the time being	

void generateArray(int randArray[], int size);
void partitionArray(int *a, int low, int high, int *pivotLocation);
void quickSort(int *a, int low, int high);

void quickSort(int *a, int low, int high){
    
	int pivotLocation;
	if(low < high){
		partitionArray(a, low, high, &pivotLocation);	
		quickSort(a, low, pivotLocation - 1);	
		quickSort(a, pivotLocation + 1, high);	
	}
}


void partitionArray(int *a, int low, int high, int *pivotLocation){
    
	int left = low;		
	int right = high;	
	*pivotLocation = left;	
	int tmp;	

	while(1){

		
		while(a[*pivotLocation] <= a[right] && *pivotLocation != right){	
			right--;	
		}

		if(*pivotLocation == right){	
			break;
		}else if(a[*pivotLocation] > a[right]){
			tmp = a[right];
			a[right] = a[*pivotLocation];
			a[*pivotLocation] = tmp;
			*pivotLocation = right;	
		}

		
		while(a[*pivotLocation] >= a[left] && *pivotLocation != left){	
			left++;		
		}

		if(*pivotLocation == left){	
			break;
		}else if(a[*pivotLocation] < a[left]){
			
			tmp = a[left];
			a[left] = a[*pivotLocation];
			a[*pivotLocation] = tmp;
			*pivotLocation = left;	
		}
	}
}

void generateArray(int randArray[], int size){

	for(int i = 0; i < size; i++){
		randArray[i] = rand() % 100;  
	}	
}

void main_blinky(void){

    int arrayToSort[ARRAY_SIZE];
    generateArray(arrayToSort, ARRAY_SIZE);

	int i;

	quickSort(arrayToSort, 0, ARRAY_SIZE-1);	

    printf("Quick sort operating: \n");

	for(i = 0; i < ARRAY_SIZE; i++){
		printf("%d ", arrayToSort[i]);
	}
    printf("\n");

    // TODO 
    TaskHandle_t TaskHandle_t;

    vTaskStartScheduler();
}

void vATaskToPivotElements(pv* parameters){

    for( ;; ){
        // TODO - add task applications here 
    }

    vTaskDelete(NULL);
}
