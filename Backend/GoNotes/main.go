package main

import (
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"net/http"
)

type CompanyStruct struct {
	ID      int    `json:"id"`
	Name    string `json:"name"`
	Country string `json:"country"`
}

type ResponseBody struct {
	Code int           `json:"code"`
	Msg  string        `json:"msg"`
	Data CompanyStruct `json:"data"`
}

type ResponseBodys struct {
	Code int                    `json:"code"`
	Msg  string                 `json:"msg"`
	Data map[string]interface{} `json:"data"`
}

var resBodyMap map[int]map[string]string = make(map[int]map[string]string)
var count int = 0
var queryKey []string = []string{"id", "name", "age"}

func main() {
	// post请求 http://localhost:9999/testPost
	http.HandleFunc("/testPost", requestTestMethods)

	// post请求 http://localhost:9999/userInfo
	http.HandleFunc("/userInfo", userInfoPost)

	// get请求 http://localhost:9999/testGet
	http.HandleFunc("/testGet", requestTestMethods)

	// 服务启动端口 http://localhost:9999
	http.ListenAndServe(":9999", nil)
}

func requestTestMethods(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	// post请求
	case http.MethodPost:
		// 把body请求参数放到json容器
		Body := json.NewDecoder(r.Body)
		companyTest := CompanyStruct{
			ID:      0,
			Name:    "",
			Country: "",
		}
		// 将请求参数解码放到结构体里面
		err := Body.Decode(&companyTest)

		// 报错
		if err != nil {
			// 错误日志
			log.Println(err.Error())
			// 响应错误码给客户端 不应该出现错误消息的响应
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		// 正常执行
		enc := json.NewEncoder(w)
		// err2 := enc.Encode(companyTest)

		resBody := ResponseBody{
			Code: 200,
			Msg:  "接口请求成功",
			Data: companyTest,
		}
		err2 := enc.Encode(resBody)

		if err2 != nil {
			// 错误日志
			log.Println(err2.Error())
			// 响应错误码给客户端 不应该出现错误消息的响应
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

	// get请求
	case http.MethodGet:
		fmt.Println("Get请求执行了", r.URL.Query())
		queryMap := r.URL.Query()
		mapBody := make(map[string]string)

		// 这种赋值方式比较局限参数个数
		// mapBody["id"] = queryMap.Get("id")
		// mapBody["name"] = queryMap.Get("name")
		// mapBody["age"] = queryMap.Get("age")

		// 使用切片配置query参数方式控制需要处理几个参数
		for _, v := range queryKey {
			mapBody[v] = queryMap.Get(v)
		}

		resBodyMap[count] = mapBody
		count++

		// 将response数据对象编码为 JSON 格式
		resDatas, _ := json.Marshal(resBodyMap)
		// 返回给浏览器
		io.WriteString(w, string(resDatas))

	default:
		w.WriteHeader(http.StatusMethodNotAllowed)
	}
}

func userInfoPost(w http.ResponseWriter, r *http.Request) {
	// 请求post
	if r.Method == http.MethodPost {
		var param map[string]interface{}
		// 读取入参
		body, _ := ioutil.ReadAll(r.Body)
		// 将body二进制入参写入到param中
		json.Unmarshal(body, &param)
		//  map[country:北京市 id:100 name:Tyler Bennett]
		// fmt.Println(param)
		// fmt.Println(param["id"], param["name"], param["country"])

		resBody := ResponseBodys{
			Code: 200,
			Msg:  "sucess",
			Data: param,
		}

		// 将response数据对象编码为 JSON 格式
		// 返回给浏览器
		b, _ := json.Marshal(resBody)
		io.WriteString(w, string(b))
	} else {
		w.WriteHeader(http.StatusMethodNotAllowed) //405 Method Not Allowed (HTTP 1.1 is the default status code for a method. It means that
	}
}
