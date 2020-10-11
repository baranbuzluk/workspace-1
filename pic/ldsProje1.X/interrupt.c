#include"interrupt.h"
void __interrupt() INTERRUPT_SERVICE_ROUTINE(void) {

    if (INTCONbits.INTF == 1) {
        changeMod();
        INTCONbits.INTF = 0;
    }
    __delay_ms(25);

}