package main

import (
	"fmt"
	"net/http"
	"time"
)

func main() {

	// 创建一个client,设置超时时间
	client := &http.Client{Timeout: time.Second * 10}

	// 构造一个GET请求
	req, err := http.NewRequest("GET", "https://www.example.com", nil)

	// 添加请求头
	req.Header.Add("User-Agent", "Go-http-client")

	// 发送请求
	resp, err := client.Do(req)

	// 检查错误
	if err != nil {
		fmt.Println("HTTP Get error:", err)
		return
	}
	defer resp.Body.Close()

	// 处理响应
	fmt.Println("Response status:", resp.Status)

	body := make([]byte, 1024)
	resp.Body.Read(body)
	fmt.Println("Response body:", string(body))
}
