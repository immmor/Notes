package main

import (
	"bytes"
	"fmt"
	"os/exec"
)

func main() {
	// 执行 Python 脚本
	cmd := exec.Command("/Users/mrok/anaconda3/bin/python", "/Users/mrok/Documents/coder/funtext/Web/Notes/notes.py")

	// 捕获输出
	var output bytes.Buffer
	cmd.Stdout = &output
	cmd.Stderr = &output

	// 执行命令
	err := cmd.Run()
	if err != nil {
		fmt.Println("Error executing Python script:", err)
		return
	}

	// 打印输出
	fmt.Println("Python script output:", output.String())
}
