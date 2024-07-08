package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
	"strings"

	"github.com/fatih/color"
)

type YoudaoResponse struct {
	Data struct {
		Entries []struct {
			Explain string `json:"explain"`
		} `json:"entries"`
	} `json:"data"`
}

var colorIndex int
var colors = []*color.Color{
	// color.New(color.FgRed),
	color.New(color.FgGreen),
	color.New(color.FgYellow),
	color.New(color.FgBlue),
	color.New(color.FgMagenta),
	color.New(color.FgCyan),
}

func transYoudao(transContent, le string) (string, error) {
	// 构建 URL 参数
	params := url.Values{}
	params.Set("num", "5")
	params.Set("ver", "3.0")
	params.Set("doctype", "json")
	params.Set("cache", "false")
	params.Set("le", le)
	params.Set("q", transContent)

	// 发送 HTTP GET 请求
	resp, err := http.Get("https://dict.youdao.com/suggest?" + params.Encode())
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	// 解析 JSON 响应
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	var youdaoResp YoudaoResponse
	err = json.Unmarshal(body, &youdaoResp)
	if err != nil {
		return "", err
	}

	// 获取翻译结果
	if len(youdaoResp.Data.Entries) > 0 {
		colorFunc := colors[colorIndex].SprintfFunc()
		colorIndex = (colorIndex + 1) % len(colors)
		return colorFunc("%s", youdaoResp.Data.Entries[0].Explain), nil
	}

	red := color.New(color.FgRed).SprintfFunc()
	return "", fmt.Errorf(red("no translation found"))
}

func main() {
	colorIndex = 0 // 重置colorIndex

	// 定义命令行参数
	transContentPtr := flag.String("text", "", "Text to be translated")
	lePtr := flag.String("lang", "en", "Language code (e.g., 'en', 'zh')")

	// 如果没有指定 --text 参数,则使用命令行参数作为翻译内容
	flag.Parse()
	transContent := *transContentPtr
	if transContent == "" && len(flag.Args()) > 0 {
		transContent = strings.Join(flag.Args(), " ")
	}

	// 检查是否提供了翻译内容
	if transContent == "" {
		red := color.New(color.FgRed).SprintfFunc()
		fmt.Println(red("Please provide the text to be translated."))
		return
	}

	// 查询有道词典 API 并输出结果
	wordExplain, err := transYoudao(transContent, *lePtr)
	if err != nil {
		red := color.New(color.FgRed).SprintfFunc()
		fmt.Println(red("Error: %v", err))
		return
	}

	fmt.Println(wordExplain)
}
