package main

import (
	"fmt"
	"os"
	"os/exec"
	"runtime"
)

func openChrome(url string) error {
	var cmd *exec.Cmd

	switch runtime.GOOS {
	case "darwin":
		cmd = exec.Command("open", "-a", "Google Chrome", url)
	case "windows":
		cmd = exec.Command("cmd", "/c", "start", "chrome", url)
	case "linux":
		chromePaths := []string{
			"google-chrome",
			"google-chrome-stable",
			"chromium",
			"chromium-browser",
		}
		for _, path := range chromePaths {
			if _, err := exec.LookPath(path); err == nil {
				cmd = exec.Command(path, url)
				break
			}
		}
		if cmd == nil {
			return fmt.Errorf("could not find Chrome on your system")
		}
	default:
		return fmt.Errorf("unsupported operating system: %s", runtime.GOOS)
	}

	return cmd.Start()
}

func main() {
	url := "https://www.baidu.com"
	err := openChrome(url)
	if err != nil {
		fmt.Printf("打开Chrome时发生错误: %v\n", err)
		os.Exit(1)
	}
	fmt.Println("已成功打开Chrome")
}
