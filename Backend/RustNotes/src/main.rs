use actix_web::{get, App, HttpResponse, HttpServer, Responder, middleware::Logger};
use env_logger;

#[get("/")]
async fn index() -> impl Responder {
    HttpResponse::Ok().body("Hello, world!")
}

#[get("/eng")]
async fn eng() -> impl Responder {
    HttpResponse::Ok().body("English learning page")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    std::env::set_var("RUST_LOG", "actix_web=info");
    env_logger::init();

    println!("Starting server on http://127.0.0.1:8000");
    HttpServer::new(|| App::new()
        .wrap(Logger::default())
        .service(index)
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