#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8888
#define BUFFER_SIZE 1024

int main() {
    int clientSocket;
    struct sockaddr_in serverAddr;

    // 创建客户端套接字
    clientSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (clientSocket == -1) {
        perror("Error creating client socket");
        exit(1);
    }

    // 初始化服务器地址结构体
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1");
    serverAddr.sin_port = htons(PORT);

    // 连接到服务器
    if (connect(clientSocket, (struct sockaddr *)&serverAddr, sizeof(serverAddr)) == -1) {
        perror("Error connecting to server");
        exit(1);
    }

    char filePath[100];
    printf("Enter the file path to upload: ");
    scanf("%s", filePath);

    // 获取文件名
    char *filename = strrchr(filePath, '/');
    if (filename == NULL) {
        filename = filePath;
    } else {
        filename++;
    }

    // 发送文件名到服务器
    send(clientSocket, filename, strlen(filename), 0);

    // 打开要上传的文件
    FILE *fp = fopen(filePath, "rb");
    if (fp == NULL) {
        perror("Error opening file for reading");
        send(clientSocket, "Error opening file", strlen("Error opening file"), 0);
        close(clientSocket);
        return 1;
    }

    char buffer[BUFFER_SIZE];
    ssize_t bytesRead;
    // 读取文件内容并发送到服务器
    while ((bytesRead = fread(buffer, 1, BUFFER_SIZE, fp)) > 0) {
        send(clientSocket, buffer, bytesRead, 0);
    }

    fclose(fp);

    // 接收服务器的响应
    recv(clientSocket, buffer, BUFFER_SIZE - 1, 0);
    buffer[BUFFER_SIZE - 1] = '\0';
    printf("%s\n", buffer);

    close(clientSocket);

    return 0;
}