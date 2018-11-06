#include <stdio.h>
#include "test.h"
#include "pretest.c"

int test (struct User_Data *A) {
    pretest(A->x) ;
#if 0
    printf ("Double is %lg\n", A->x) ;
#endif
    printf ("Int is %i\n", A->n) ;
    
    return A->n ;
}
