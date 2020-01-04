#include<stdio.h>
#include<arpa/inet.h>
/**将char类型逐个打印成十六进制形式**/
void stringToHex(char *string,unsigned int len)
{
    unsigned int loop = 0;
    char *temp = string;
    if(NULL == temp)
    {
        printf("input para is NULL\n");
        return;
    }
    for(loop = 0; loop < len; loop++)
    {
        printf("%p:0x%2x\n",temp,*(temp)); //4个字节意味着4个地址，依次打印每个地址和相应的数据
        temp++;
    }

}
int main(int argc,char *argv[])
{
    /**x86为小端序**/
    printf("转换之前\n");
    int a = 0x12345678; // 0x12345678, 16进制，每个数字占有4bit，共占有32bit，正好是4个字节的长度
    printf("a = %d\n",a);
    stringToHex((char*)&a,sizeof(int));
    /*转为网络字节序之后再打印*/
    printf("转换之后\n");
    a = htonl(a);/*转换为网络序*/
    printf("a = %d\n",a);
    stringToHex((char*)&a,sizeof(int));
    return 0 ;
}
