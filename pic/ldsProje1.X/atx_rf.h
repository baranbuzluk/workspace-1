/* 
 * File:   atx_rf.h
 * Author: User
 *
 * Created on 04 Eylül 2020 Cuma, 10:37
 */

#ifndef ATX_RF_H
#define	ATX_RF_H

#ifdef	__cplusplus
extern "C" {
#endif
#include"init.h"
#define PREAMBLE 0x55
#define SECRON_0 0x00
#define SECRON_1 0xFF
#define PREPARATION_SIZE 15
#define DELAY_uS 1
    unsigned char preparation[15] = {PREAMBLE, PREAMBLE, PREAMBLE, PREAMBLE, PREAMBLE,
                                    SECRON_0, SECRON_0, SECRON_0, SECRON_0, SECRON_0,
                                    SECRON_1, SECRON_1, SECRON_1, SECRON_1, SECRON_1};
    void sendData(Byte_t data);
#ifdef	__cplusplus
}
#endif

#endif	/* ATX_RF_H */

