/* 
 * File:   interrupt.h
 * Author: PC
 *
 * Created on 01 Eylül 2020 Sal?, 17:18
 */

#ifndef INTERRUPT_H
#define	INTERRUPT_H

#ifdef	__cplusplus
extern "C" {
#endif

#include"init.h"
void __interrupt() INTERRUPT_SERVICE_ROUTINE(void);

#ifdef	__cplusplus
}
#endif

#endif	/* INTERRUPT_H */

