#include <windows.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <psapi.h>

#pragma comment(lib, "psapi.lib")
#pragma comment(lib, "user32.lib")

#define VERSION "0.020"
#define FILENAME "u.txt"

HANDLE hConsole;

void cls() {
    system("cls");
}

void setColor(int color) {
    SetConsoleTextAttribute(hConsole, color);
}

void writeUsername(const char* name) {
    FILE* f = fopen(FILENAME, "w");
    if (f) {
        fprintf(f, "%s", name);
        fclose(f);
    }
}

int readUsername(char* buffer, int size) {
    FILE* f = fopen(FILENAME, "r");
    if (f) {
        if (fgets(buffer, size, f)) {
            size_t len = strlen(buffer);
            if (len > 0 && buffer[len-1] == '\n') buffer[len-1] = '\0';
            fclose(f);
            return 1;
        }
        fclose(f);
    }
    return 0;
}

void beep() {
    Beep(700, 500);
}

void beeep() {
    Beep(900, 300);
    Beep(1300, 300);
}

int main() {
    char name[256];
    char cmd[256];
    char newname[256];
    char text[256];
    char aquest[10];
    
    hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    
    if (!readUsername(name, sizeof(name))) {
        setColor(10);
        printf("get.username:;\n");
        Sleep(500);
        printf("get.username = err:\n");
        Sleep(100);
        printf("start(), get:\n");
        Sleep(50);
        printf("start - True:\n");
        Sleep(100);
        printf("check.startlist:\n");
        Sleep(500);
        printf("get.all.startlist:\n");
        Sleep(100);
        printf("startlist:\ninput('username')\nafter.input('username')\nlambda.startlist(get(True)))\n");
        Sleep(100);
        printf("lambda: run.startlist.directly = True;\n");
        Sleep(100);
        cls();
        
        while (1) {
            setColor(10);
            printf("l: ");
            setColor(7);
            printf("enter your username\n");
            Beep(1000, 300);
            Beep(1300, 400);
            setColor(14);
            printf("lingua: ");
            setColor(7);
            fgets(name, sizeof(name), stdin);
            name[strcspn(name, "\n")] = 0;
            
            if (strlen(name) > 0) {
                writeUsername(name);
                break;
            } else {
                setColor(12);
                printf("err: ");
                setColor(7);
                printf("username not defined\n");
                Beep(500, 500);
            }
        }
    }
    
    cls();
    setColor(7);
    printf("hi, %s!\n", name);
    Beep(1100, 450);
    Beep(1300, 700);
    
    while (1) {
        setColor(14);
        printf("jungua");
        setColor(10);
        printf("@");
        setColor(7);
        printf("%s: ", name);
        fgets(cmd, sizeof(cmd), stdin);
        cmd[strcspn(cmd, "\n")] = 0;
        Beep(1500, 200);
        
        if (strcmp(cmd, "whoami") == 0) {
            setColor(14);
            printf("your username: ");
            setColor(7);
            printf("%s\n", name);
        }
        else if (strcmp(cmd, "exit") == 0) {
            break;
        }
        else if (strcmp(cmd, "fetch") == 0) {
            MEMORYSTATUSEX memStatus;
            memStatus.dwLength = sizeof(memStatus);
            GlobalMemoryStatusEx(&memStatus);
            
            DWORD drives = GetLogicalDrives();
            char drivePath[] = "C:\\";
            ULARGE_INTEGER freeBytes, totalBytes;
            GetDiskFreeSpaceExA(drivePath, &freeBytes, &totalBytes, NULL);
            
            double diskgb = (double)totalBytes.QuadPart / (1024.0 * 1024.0 * 1024.0);
            double ramgb = (double)memStatus.ullTotalPhys / (1024.0 * 1024.0 * 1024.0);
            
            time_t now;
            time(&now);
            struct tm *local = localtime(&now);
            
            setColor(14);
            printf("\n             ###########\n");
            printf("              #########\n");
            printf("              #########\n");
            printf("             ###########\n");
            printf("             \n");
            printf("             ###########\n");
            printf("              #########\n");
            printf("              #########\n");
            printf("              #########\n");
            printf("              #########\n");
            printf("    ######    #########\n");
            printf("   ######## ##########\n");
            printf("     ################\n");
            printf("        #########\n\n");
            
            setColor(7);
            setColor(14);
            printf("version: ");
            setColor(7);
            printf("%s\n", VERSION);
            setColor(14);
            printf("disk storage: ");
            setColor(7);
            printf("%.2fGB\n", diskgb);
            setColor(14);
            printf("ram storage: ");
            setColor(7);
            printf("%.2fGB\n", ramgb);
            setColor(14);
            printf("time now: ");
            setColor(7);
            printf("%04d-%02d-%02d %02d:%02d:%02d\n", 
                   local->tm_year + 1900, local->tm_mon + 1, local->tm_mday,
                   local->tm_hour, local->tm_min, local->tm_sec);
        }
        else if (strcmp(cmd, "clear") == 0 || strcmp(cmd, "cls") == 0) {
            cls();
        }
        else if (strncmp(cmd, "say(", 4) == 0 && cmd[strlen(cmd)-1] == ')') {
            strcpy(text, cmd + 4);
            text[strlen(text)-1] = '\0';
            setColor(10);
            printf("%s\n", text);
            setColor(7);
        }
        else if (strcmp(cmd, "rename") == 0) {
            beeep();
            setColor(10);
            printf("rename: ");
            setColor(7);
            fgets(newname, sizeof(newname), stdin);
            newname[strcspn(newname, "\n")] = 0;
            
            if (strlen(newname) == 0) {
                setColor(12);
                printf("err: ");
                setColor(7);
                printf("username not defined\n");
                Beep(500, 500);
                continue;
            }
            
            beep();
            setColor(12);
            printf("do you really want to rename?\n");
            setColor(14);
            printf("before rename: ");
            setColor(7);
            printf("%s\n", name);
            setColor(14);
            printf("after rename: ");
            setColor(7);
            printf("%s\n", newname);
            setColor(8);
            printf("(y/n) ");
            setColor(7);
            fgets(aquest, sizeof(aquest), stdin);
            
            if (aquest[0] == 'y' || aquest[0] == 'Y') {
                if (strcmp(newname, name) == 0) {
                    setColor(14);
                    printf("info: ");
                    setColor(7);
                    printf("this is already your name\n");
                    Beep(800, 300);
                    continue;
                } else {
                    writeUsername(newname);
                    strcpy(name, newname);
                    Beep(1000, 300);
                    Beep(1200, 300);
                }
            } else {
                setColor(14);
                printf("rename cancelled\n");
                setColor(7);
                Beep(600, 300);
            }
        }
        else if (strcmp(cmd, "help") == 0) {
            beep();
            setColor(12);
            printf("check ");
            setColor(14);
            printf("'README.md' ");
            setColor(12);
            printf("on official repository: ");
            setColor(8);
            printf("https://github.com/arxxdd-scheg/jungua\n");
            setColor(7);
        }
    }
    
    return 0;
}
