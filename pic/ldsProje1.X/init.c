/*
 * File:   init.c
 * Author: PC
 *
 * Created on 01 Eyl�l 2020 Sal?, 10:14
 */
#include"init.h"

void initInterrupt() {
    OPTION_REGbits.INTEDG = 1;
    INTCONbits.GIE = 1;
    INTCONbits.PEIE = 1;
    INTCONbits.INTE = 1;
}
void initGPIO() {
    TRISIObits.TRISIO1 = 0;
    TRISIObits.TRISIO4 = 0;
    TRISIObits.TRISIO2 = 1;
    CMCON = 0x07;
    ANSEL = 0;
    GPIO = 0;
}