use actix_web::{get, App, HttpRequest, HttpResponse, HttpServer, Responder, middleware::Logger};
use actix_files::NamedFile;
use std::path::PathBuf;
use env_logger;

#[get("/")]
async fn index() -> impl Responder {
    HttpResponse::Ok().body("Hello, world!")
}

// #[get("/mm")]
// async fn mm() -> impl Responder {
//     // 读取 HTML 文件
//     let html_content = std::fs::read_to_string(r"F:\VSCode Files\Web\Notes\Backend\RustNotes\src\index.html").unwrap();
//     html_content
// }

#[get("/mm")]
async fn mm(req: HttpRequest) -> Result<NamedFile> {
    let path: PathBuf = req.match_info().query(r"F:\VSCode Files\Web\Notes\Backend\RustNotes\src\index.html").parse().unwrap();
    Ok(NamedFile::open(path)?)
}

#[get("/eng")]
async fn eng() -> impl Responder {
    HttpResponse::Ok().body("English learning page")
}

#[get("/ai")]
async fn ai() -> impl Responder {
    HttpResponse::Ok().body("AI learning page")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    std::env::set_var("RUST_LOG", "actix_web=info");
    env_logger::init();

    println!("Starting server on http://127.0.0.1:8000");
    HttpServer::new(|| App::new()
        .wrap(Logger::default())
        .service(index)
        .service(mm)
        .service(ai)
        .service(eng))
    .bind("127.0.0.1:8000")?
    .run()
    .await
}




// use actix_web::{get, middleware::Logger, App, HttpServer, Responder, HttpResponse};
// use env_logger;
// use std::path::PathBuf;

// #[get("/")]
// async fn index() -> impl Responder {
//     let path = PathBuf::from("./index.html");
//     actix_files::NamedFile::open(path).unwrap()
//     // match actix_files::NamedFile::open(path) {
//     //     Ok(file) => file,
//     //     Err(err) => {
//     //         println!("Error opening file: {}", err);
//     //         HttpResponse::NotFound().body("File not found")
//     //     }
//     // }
// }

// #[get("/eng")]
// async fn eng() -> impl Responder {
//     let path = PathBuf::from("./index.html");
//     actix_files::NamedFile::open(path).unwrap()
// }

// #[actix_web::main]
// async fn main() -> std::io::Result<()> {
//     std::env::set_var("RUST_LOG", "actix_web=info");
//     env_logger::init();

//     println!("Starting server on http://127.0.0.1:8000");
//     HttpServer::new(|| {
//         App::new()
//             .wrap(Logger::default())
//             .service(index)
//             .service(eng)
//     })
//     .bind("127.0.0.1:8000")?
//     .run()
//     .await
// }