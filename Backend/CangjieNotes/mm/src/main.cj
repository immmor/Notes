from net import http.ServerBuilder, http.FuncHandler

main() {
    let server = ServerBuilder().addr("127.0.0.1").port(8888).build()

    server.distributor.register("/user/info", FuncHandler({httpContext =>
        println("user info come here")
        httpContext.responseBuilder.body("hello this is user info")
    }))

    server.distributor.register("/user/list", FuncHandler({httpContext =>
        println("user list come here")
        httpContext.responseBuilder.body("hello this is user list")
    }))

    server.serve()
}