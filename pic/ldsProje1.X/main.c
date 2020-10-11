#include"init.h"

extern unsigned char mode;

void main(void) {
    initGPIO();
    initInterrupt();
    while (1) {
        if (mode == LOW) {
            ledYakMod1();
        } else {
            ledYakMod4();
        }
    }
    return;
}
