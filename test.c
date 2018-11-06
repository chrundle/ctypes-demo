#include <stdio.h>
#include "test.h"
#include "pretest.c"

int test (struct User_Data *A) {
    /* Initialize variables */
    double a, b ;
    a = 7.5 ;
    b = 3.0 ;

    /* Evaluate function f_value from A */
    A->f_value(a,b) ;

    pretest(A->x) ;
#if 0
    printf ("Double is %lg\n", A->x) ;
#endif
    printf ("Int is %i\n", A->n) ;
    
    return A->n ;
}
