package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	/*
		router.GET("/Get", getting)
		router.POST("/Post", posting)
		router.PUT("/Put", putting)
		router.DELETE("/Delete", deleting)
		router.PATCH("/Patch", patching)
		router.HEAD("/Head", head)
		router.OPTIONS("/Options", options)
	*/
	router.GET("/Get", func(context *gin.Context) {
		context.JSON(200, gin.H{
			"message": "get",
		})
	})
	router.POST("/Post", func(context *gin.Context) {
		context.JSON(200, gin.H{
			"message": "post",
		})
	})
	router.PUT("/put", func(context *gin.Context) {
		context.JSON(200, gin.H{
			"message": "put",
		})
	})
	router.DELETE("/Delete", func(context *gin.Context) {
		context.JSON(200, gin.H{
			"message": "delete",
		})
	})
	router.PATCH("/Patch", func(context *gin.Context) {
		context.JSON(200, gin.H{
			"message": "patch",
		})
	})
	router.HEAD("/Head", func(context *gin.Context) {
		context.JSON(200, gin.H{
			"message": "head",
		})
	})
	router.OPTIONS("/Options", func(context *gin.Context) {
		context.JSON(200, gin.H{
			"message": "options",
		})
	})
	// 默认启动的是 8080端口，也可以自己定义启动端口
	router.Run(":1009")
}
