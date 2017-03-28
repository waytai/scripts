//linux c定时执行程序
#include <stdio.h> //printf()
#include <unistd.h> //pause()
#include <signal.h> //signal()
#include <string.h> //memset()
#include <sys/time.h> //struct itimerval, setitimer()
void printMsg(int);
int main(void)
{
    int res = 0;
    struct itimerval tick;
    signal( SIGALRM, printMsg );
    memset( &tick, 0, sizeof(tick) );
    tick.it_value.tv_sec = 1;
    tick.it_value.tv_usec = 0;
    tick.it_interval.tv_sec = 10;
    tick.it_interval.tv_usec = 0;
    res = setitimer( ITIMER_REAL, &tick, NULL );
    if( res ){
        printf( "set timer failed\n" );
    }
    //int i = 5;
    while( 1 ){
        pause();
    }
    return 0;
}
void printMsg(int sig)
{
    printf( "Hello, world !\n" );
}
