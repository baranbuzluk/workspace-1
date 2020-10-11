/* 
 * File:   init.h
 * Author: PC
 *
 * Created on 01 Eylül 2020 Sal?, 10:09
 */

#ifndef INIT_H
#define	INIT_H

#ifdef	__cplusplus
extern "C" {
#endif

#include<xc.h>
#include<pic12f675.h>
#include"led_kontrol.h"
#include"interrupt.h"
    
#pragma config FOSC=INTRCIO,WDTE=OFF,MCLRE=OFF,BOREN=OFF
#define _XTAL_FREQ 4000000
#define LOW 0
#define HIGH 1    
typedef unsigned char Byte_t;
    void initInterrupt();
    void initGPIO();
    

#ifdef	__cplusplus
}
#endif

#endif	/* INIT_H */

