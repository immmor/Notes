#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>

void getTXTFiles(const std::string& path, std::ofstream& fp) {
    std::filesystem::path searchPath(path);
    for (const auto& entry : std::filesystem::directory_iterator(searchPath)) {
        if (entry.is_directory()) {
            if (entry.path().filename() != "." && entry.path().filename() != "..") {
                std::string newpath = entry.path().string();
                getTXTFiles(newpath, fp);
            }
        } else {
            std::string extension = entry.path().extension().string();
            if (extension == ".txt") {
                fp << entry.path().string() << std::endl;
            }
        }
    }
}

int main() {
    std::ofstream fp("4.txt");
    if (!fp) {
        std::cerr << "Failed to open file." << std::endl;
        return 1;
    }

    getTXTFiles("c:\\", fp);

    fp.close();
    return 0;
}