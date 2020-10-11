/* 
 * File:   led_kontrol.h
 * Author: PC
 *
 * Created on 01 Eylül 2020 Sal?, 10:17
 */

#ifndef LED_KONTROL_H
#define	LED_KONTROL_H

#ifdef	__cplusplus
extern "C" {
#endif
#include"init.h"
    void toggleGP1();
    void toggleGP4();
    void changeMod();
    void ledYakMod1();
    void ledYakMod2();
    void ledYakMod3();
    void ledYakMod4();
    
    // DEFINE MACRO
    unsigned char count;
#define __OnOffGP4(tekrar,delay_ms) count=tekrar; while (count--) {\
        toggleGP4(); __delay_ms(delay_ms); toggleGP4();__delay_ms(delay_ms+50);}\

#define __OnOffGP1(tekrar,delay_ms) count=tekrar; while (count--) {\
        toggleGP1(); __delay_ms(delay_ms); toggleGP1();__delay_ms(delay_ms);}\
    // DEFINE MACRO

#ifdef	__cplusplus
}
#endif

#endif	/* LED_KONTROL_H */

