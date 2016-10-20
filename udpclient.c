/*************************************************************************
    > File Name: udpclient.c
    > Author: wayne
    > Mail: @163.com 
    > Created Time: 2016年10月20日 星期四 14时14分09秒
 ************************************************************************/
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <strings.h>
#include <string.h>
#define PORT 11168
int main()
{
    char buf[6];
    int sockfd;
    int len;
    int ret;
    struct sockaddr_in server_addr;
    sockfd=socket(AF_INET, SOCK_DGRAM, 0);
    if(sockfd==-1)
    {
        perror("创建SOCK失败！");
        return(-1);
    }

    
    server_addr.sin_family=AF_INET;
    server_addr.sin_port=htons(PORT);
    server_addr.sin_addr.s_addr=inet_addr("192.168.0.1");
    bzero((void *)&(server_addr.sin_zero), (size_t)8);
    len=sizeof(server_addr);


    strcpy(buf, "Hello");
    sendto(sockfd, buf, sizeof(buf), 0, (struct sockaddr *)&server_addr, len);
    close(sockfd);
    return(0);
}
    
