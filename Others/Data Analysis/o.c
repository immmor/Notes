#include <stdio.h>
#include <string.h>
#include <dirent.h>

void getTXTFiles(const char *path, FILE *fp) {
    DIR *dir;
    struct dirent *entry;

    dir = opendir(path);
    if (dir == NULL) {
        return;
    }

    while ((entry = readdir(dir)) != NULL) {
        if (entry->d_type == DT_DIR) {
            if (strcmp(entry->d_name, ".") != 0 && strcmp(entry->d_name, "..") != 0) {
                char newpath[PATH_MAX];
                snprintf(newpath, sizeof(newpath), "%s/%s", path, entry->d_name);
                getTXTFiles(newpath, fp);
            }
        } else {
            char *p = strrchr(entry->d_name, '.');
            if (p != NULL && strcmp(p, ".txt") == 0) {
                fprintf(fp, "%s/%s\n", path, entry->d_name);
            }
        }
    }

    closedir(dir);
}

int main() {
    FILE *fp = fopen("1.txt", "w");
    if (fp == NULL) {
        perror("fopen");
        return 1;
    }

    getTXTFiles("c:/", fp);

    fclose(fp);
    return 0;
}