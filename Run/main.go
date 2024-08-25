package main

import (
	"bytes"
	"fmt"
	"os/exec"
	"runtime"
)

func main() {
	// 执行 Python 脚本
	var cmd *exec.Cmd

	switch runtime.GOOS {
	case "darwin":
		fmt.Println("This is a Mac system.")
		dir := "/Users/mrok/Documents/coder/funtext/Web/Notes/"
		cmd = exec.Command("/Users/mrok/anaconda3/bin/python",
			"/Users/mrok/Documents/coder/funtext/Web/Notes/notes.py")
		cmd.Dir = dir
	case "windows":
		fmt.Println("This is a Windows system.")
		dir := "f:/VSCode Files/Web/Notes/"
		cmd = exec.Command("F:/anaconda3/python.exe",
			"f:/VSCode Files/Web/Notes/notes.py")
		cmd.Dir = dir
	}
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
