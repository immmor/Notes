#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8888
#define BUFFER_SIZE 1024

int main() {
    int serverSocket, clientSocket;
    struct sockaddr_in serverAddr, clientAddr;
    socklen_t addrLen = sizeof(clientAddr);

    // 创建服务器套接字
    serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket == -1) {
        perror("Error creating server socket");
        exit(1);
    }

    // 初始化服务器地址结构体
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = INADDR_ANY;
    serverAddr.sin_port = htons(PORT);

    // 绑定服务器套接字到指定端口
    if (bind(serverSocket, (struct sockaddr *)&serverAddr, sizeof(serverAddr)) == -1) {
        perror("Error binding server socket");
        exit(1);
    }

    // 监听客户端连接
    if (listen(serverSocket, 5) == -1) {
        perror("Error listening for connections");
        exit(1);
    }

    printf("Server listening on port %d...\n", PORT);

    // 接受客户端连接
    clientSocket = accept(serverSocket, (struct sockaddr *)&clientAddr, &addrLen);
    if (clientSocket == -1) {
        perror("Error accepting client connection");
        exit(1);
    }

    printf("Client connected.\n");

    char buffer[BUFFER_SIZE];
    // 接收文件名
    recv(clientSocket, buffer, BUFFER_SIZE - 1, 0);
    buffer[BUFFER_SIZE - 1] = '\0';
    char *filename = buffer;

    // 打开文件用于写入
    FILE *fp = fopen(filename, "wb");
    if (fp == NULL) {
        perror("Error opening file for writing");
        send(clientSocket, "Error opening file", strlen("Error opening file"), 0);
        close(clientSocket);
        close(serverSocket);
        return 1;
    }

    // 接收文件内容并写入文件
    ssize_t bytesRead;
    while ((bytesRead = recv(clientSocket, buffer, BUFFER_SIZE, 0)) > 0) {
        fwrite(buffer, 1, bytesRead, fp);
    }

    fclose(fp);

    // 发送上传成功消息
    send(clientSocket, "File uploaded successfully", strlen("File uploaded successfully"), 0);

    close(clientSocket);
    close(serverSocket);

    return 0;
}