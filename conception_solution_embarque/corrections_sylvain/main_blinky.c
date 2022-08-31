#include "FreeRTOS.h"
#include "task.h"
#include <time.h>

#define MAX_TASK (1 << 7)
#define ARRAY_SIZE (1 << 20)

void vSort(void* pvParameters);
void vPivot(int first, int last, int taskId, int lastId);

int data[ARRAY_SIZE];

struct Parameter {
    int first, last, lastId;
};
static struct Parameter parameters[MAX_TASK] = {
    { 0, ARRAY_SIZE - 1, MAX_TASK - 1 }
};

void main_blinky(void) {
    srand(time(NULL));

    for (int i = 0; i < ARRAY_SIZE; i++) {
        data[i] = rand();
    }
    TaskHandle_t taskHandle;

    xTaskCreate(vSort, "", 50, (void*)0, 1, &taskHandle);

    vTaskStartScheduler();
}

void vSort(void* pvParameters) {
    int taskId = (int)pvParameters;
    struct Parameter params = parameters[taskId];

    vPivot(params.first, params.last, taskId, params.lastId);
    if (taskId == 0) {
        while (uxTaskGetNumberOfTasks() > 1) {
            vTaskDelay(1 * portTICK_PERIOD_MS);
        }
        // AFAIRE calculer et afficher la durée (et le nombre de tâches)
        // AFAIRE afficher le tableau
        printf("Fin du tri");
    }
    vTaskDelete(NULL);
}

void vPivot(int first, int last, int taskId, int lastId) {
    portTickType start = xTaskGetTickCount();
    int pos = first;

    // AFAIRE : condition d'arrêt et Faire la répartition
    if (1) {
        return;
    }

    // Répartition du tableau de gauche
    if (taskId != lastId) {
        TaskHandle_t taskHandle;
        int newTaskId = (taskId + lastId + 1) / 2;

        parameters[newTaskId].first = first;
        parameters[newTaskId].last = pos - 1;
        parameters[newTaskId].lastId = lastId;
        lastId = newTaskId - 1;
        // AFAIRE Créer la tâche pour répartir le tableau de gauche
    }
    else {
        // AFAIRE Appel récursif pour répartir le tableau de gauche
    }
    // Répartition du tableau de droite
    vPivot(pos + 1, last, taskId, lastId);
}

