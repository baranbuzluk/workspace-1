/*
 * File:   led_kontrol.c
 * Author: PC
 *
 * Created on 01 Eylül 2020 Sal?, 10:17
 */

#include"led_kontrol.h"

unsigned char mode = 0;

void toggleGP4() {
    if (GPIObits.GP4) {
        GPIObits.GP4 = 0;
    } else {
        GPIObits.GP4 = 1;
        
    }
}

void toggleGP1() {
    if (GPIObits.GP1) {
        GPIObits.GP1 = 0;
    } else {
        GPIObits.GP1 = 1;
    }
}



void changeMod() {
    if (mode == 0)
        mode = 1;
    else
        mode = 0;
}

void ledYakMod1() {
    __OnOffGP1(5, 50);
    __OnOffGP4(5, 50);
}

void ledYakMod2() {
    __OnOffGP1(1, 25);
    __OnOffGP1(1, 25);
    __OnOffGP1(2, 100);
    __OnOffGP1(2, 100);
    __OnOffGP1(1, 25);
    __OnOffGP1(1, 25);
    

    
    __OnOffGP4(1, 25);
    __OnOffGP4(1, 25);
    __OnOffGP4(2, 100);
    __OnOffGP4(2, 100);
    __OnOffGP4(1, 25);
    __OnOffGP4(1, 25);
}

void ledYakMod3() {
    __OnOffGP1(10, 10);
    __OnOffGP1(5, 30);
    __OnOffGP1(2, 75);
    __OnOffGP1(5, 30);
    __OnOffGP1(10, 10);



    __OnOffGP4(10, 10);
    __OnOffGP4(5, 30);
    __OnOffGP4(2, 75);
    __OnOffGP4(5, 30);
    __OnOffGP4(10, 10);
}

void ledYakMod4() {
    __OnOffGP1(4, 50);
    __OnOffGP1(4, 25);
    __OnOffGP1(2, 15);
    __OnOffGP1(2, 15);
    __OnOffGP1(4, 25);
    __OnOffGP1(4, 50);


    __OnOffGP4(4, 100);
    __OnOffGP4(10, 25);
}
