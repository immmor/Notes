#include <stdio.h>
#include <string.h>
#include <windows.h>

void getTXTFiles(const char *path, FILE *fp) {
    char searchPath[MAX_PATH];
    WIN32_FIND_DATA findData;
    HANDLE hFind;

    snprintf(searchPath, sizeof(searchPath), "%s\\*", path);
    hFind = FindFirstFile(searchPath, &findData);
    if (hFind == INVALID_HANDLE_VALUE) {
        return;
    }

    do {
        if (findData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            if (strcmp(findData.cFileName, ".") != 0 && strcmp(findData.cFileName, "..") != 0) {
                char newpath[MAX_PATH];
                snprintf(newpath, sizeof(newpath), "%s\\%s", path, findData.cFileName);
                getTXTFiles(newpath, fp);
            }
        } else {
            char *p = strrchr(findData.cFileName, '.');
            if (p != NULL && strcmp(p, ".txt") == 0) {
                fprintf(fp, "%s\\%s\n", path, findData.cFileName);
            }
        }
    } while (FindNextFile(hFind, &findData) != 0);

    FindClose(hFind);
}

int main() {
    FILE *fp = fopen("2.txt", "w");
    if (fp == NULL) {
        perror("fopen");
        return 1;
    }

    getTXTFiles("c:\\", fp);

    fclose(fp);
    return 0;
}